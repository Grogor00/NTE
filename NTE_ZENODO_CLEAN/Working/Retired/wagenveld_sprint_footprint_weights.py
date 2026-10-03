#!/usr/bin/env python3
"""HEALPix footprint weights for Wagenveld sprint §5.4 sky integrals.

Ring-centre pixel projection via astropy-healpix (healpy pip build fails on
Win/Python 3.13; astropy-healpix matches healpy ring convention — validated
against Scratch §5.4: northern b>=0 mask at Nside=8 gives P=0.3234).

Output: wagenveld_sprint_footprints_nside16.json (+ optional FITS masks)

Scratch uses: Delta D_S ~ A * integral W(n)(n.n_pref) / integral W(n)
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import astropy.units as u
import numpy as np
from astropy.coordinates import Galactic, SkyCoord
from astropy_healpix import HEALPix

NSIDE = 16
KAPPA0 = 0.55  # §5.2 closure; A_frac = delta_eps / (1 + kappa0)

# LoTSS-DR2 contiguous regions (Shimwell et al. 2022, A&A 659, A1)
# 5634 deg2 total ≈ 27% northern sky; pointings at |b| > 20° (V-LoTSS 2023)
LOTSS_REGIONS_ICRS = [
    {"name": "RA-13", "ra_deg": 191.25, "dec_deg": 44.5, "radius_deg": 38.9, "area_deg2": 4178},
    {"name": "RA-1", "ra_deg": 15.0, "dec_deg": 28.0, "radius_deg": 21.6, "area_deg2": 1457},
]
LOTSS_LITERATURE_F_SKY = 5634.0 / 41253.0
LOTSS_GAL_LAT_MIN_DEG = 20.0

GALACTIC_CUTS = {
    "catwise": 10.0,   # common |b| cut in dipole studies (Secrest et al. lineage)
    "quaia": 20.0,     # QSO catalogues often mask |b| < 20°
    "singal": 10.0,    # composite radio; near-uniform beyond Galactic plane
}


def lb_to_unit_vec(l_deg: float, b_deg: float) -> tuple[float, float, float]:
    l_rad, b_rad = math.radians(l_deg), math.radians(b_deg)
    cb = math.cos(b_rad)
    return cb * math.cos(l_rad), cb * math.sin(l_rad), math.sin(b_rad)


def dipole_projection(
    weights: list[float],
    l_arr: np.ndarray,
    b_arr: np.ndarray,
    n_pref_l: float,
    n_pref_b: float,
) -> float:
    n_pref = lb_to_unit_vec(n_pref_l, n_pref_b)
    dot_sum = w_sum = 0.0
    for w, l_deg, b_deg in zip(weights, l_arr, b_arr):
        if w <= 0:
            continue
        v = lb_to_unit_vec(l_deg, b_deg)
        dot_sum += w * sum(a * b for a, b in zip(v, n_pref))
        w_sum += w
    return dot_sum / w_sum if w_sum else 0.0


def healpix_pixel_galactic(nside: int) -> tuple[HEALPix, np.ndarray, np.ndarray, np.ndarray]:
    hp = HEALPix(nside=nside, order="ring")
    npix = hp.npix
    ipix = np.arange(npix)
    lon, lat = hp.healpix_to_lonlat(ipix)
    gal = Galactic(l=lon, b=lat)
    return hp, gal.l.deg, gal.b.deg, ipix


def mask_lotss(l_arr: np.ndarray, b_arr: np.ndarray, pix_gal: SkyCoord) -> list[float]:
    weights = []
    for b_deg, coord in zip(b_arr, pix_gal):
        if abs(b_deg) < LOTSS_GAL_LAT_MIN_DEG:
            weights.append(0.0)
            continue
        inside = False
        for reg in LOTSS_REGIONS_ICRS:
            ctr = SkyCoord(
                ra=reg["ra_deg"] * u.deg,
                dec=reg["dec_deg"] * u.deg,
                frame="icrs",
            )
            if ctr.separation(coord) <= reg["radius_deg"] * u.deg:
                inside = True
                break
        weights.append(1.0 if inside else 0.0)
    return weights


def mask_galactic_cut(b_arr: np.ndarray, cut_deg: float) -> list[float]:
    return [1.0 if abs(b) >= cut_deg else 0.0 for b in b_arr]


def load_surveys_meta() -> dict:
    path = Path(__file__).with_name("wagenveld_sprint_surveys.json")
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def delta_d_band(projection: float, delta_eps_low: float = 1e-3, delta_eps_high: float = 1e-2) -> dict:
    """§5.2 fractional ΔD_S band from δε range."""
    a_low = delta_eps_low / (1.0 + KAPPA0)
    a_high = delta_eps_high / (1.0 + KAPPA0)
    return {
        "delta_eps_low": delta_eps_low,
        "delta_eps_high": delta_eps_high,
        "A_frac_low": round(a_low, 6),
        "A_frac_high": round(a_high, 6),
        "delta_D_low": round(a_low * projection, 6),
        "delta_D_high": round(a_high * projection, 6),
    }


def write_fits_masks(
    out_dir: Path,
    nside: int,
    survey_weights: dict[str, list[float]],
) -> list[str]:
    """Optional HEALPix FITS masks (one HDU per survey)."""
    try:
        from astropy.io import fits
    except ImportError:
        return []

    paths = []
    for sid, weights in survey_weights.items():
        path = out_dir / f"wagenveld_sprint_mask_{sid}_nside{nside}.fits"
        hdu = fits.PrimaryHDU(data=np.array(weights, dtype=np.float32))
        hdu.header["NSIDE"] = nside
        hdu.header["ORDERING"] = "RING"
        hdu.header["SURVEY"] = sid
        hdu.writeto(path, overwrite=True)
        paths.append(str(path.name))
    return paths


def build_footprints(nside: int = NSIDE, write_fits: bool = True) -> dict:
    meta = load_surveys_meta()
    ref = meta["reference_frames"]
    n_pref_l = ref["cmb_kinematic_dipole_l_deg"]
    n_pref_b = ref["cmb_kinematic_dipole_b_deg"]

    _, l_arr, b_arr, _ = healpix_pixel_galactic(nside)
    npix = 12 * nside * nside
    pix_gal = SkyCoord(l=l_arr * u.deg, b=b_arr * u.deg, frame=Galactic)

    survey_by_id = {s["id"]: s for s in meta["surveys"]}

    mask_builders = {
        "wagenveld": lambda: mask_lotss(l_arr, b_arr, pix_gal),
        "catwise": lambda: mask_galactic_cut(b_arr, GALACTIC_CUTS["catwise"]),
        "quaia": lambda: mask_galactic_cut(b_arr, GALACTIC_CUTS["quaia"]),
        "singal": lambda: mask_galactic_cut(b_arr, GALACTIC_CUTS["singal"]),
    }

    survey_weights: dict[str, list[float]] = {}
    surveys_out: dict[str, dict] = {}

    for sid, builder in mask_builders.items():
        w = builder()
        survey_weights[sid] = w
        proj = dipole_projection(w, l_arr, b_arr, n_pref_l, n_pref_b)
        w_sum = sum(w)
        f_sky = w_sum / npix
        sm = survey_by_id.get(sid, {})
        fp = sm.get("footprint", {})

        prov = {
            "wagenveld": (
                "LoTSS-DR2 two-region spherical-cap approximation "
                f"(Shimwell et al. 2022; {LOTSS_LITERATURE_F_SKY:.3f} f_sky literature); "
                f"|b| >= {LOTSS_GAL_LAT_MIN_DEG}°"
            ),
            "catwise": f"Galactic latitude cut |b| >= {GALACTIC_CUTS['catwise']}° (all-sky WISE selection)",
            "quaia": f"Galactic latitude cut |b| >= {GALACTIC_CUTS['quaia']}° (Gaia+unWISE QSO)",
            "singal": f"Galactic latitude cut |b| >= {GALACTIC_CUTS['singal']}° (multi-survey composite proxy)",
        }[sid]

        surveys_out[sid] = {
            "label": sm.get("label", sid),
            "dipole_projection": round(proj, 6),
            "f_sky_computed": round(f_sky, 4),
            "f_sky_literature": fp.get("f_sky"),
            "weight_sum": round(w_sum, 2),
            "dipole_l_deg": sm.get("dipole_l_deg"),
            "dipole_b_deg": sm.get("dipole_b_deg"),
            "dipole_sigma_deg": sm.get("dipole_sigma_deg"),
            "direction_source": sm.get("direction_source"),
            "mask_provenance": prov,
            "delta_D_band": delta_d_band(proj),
            "weights_healpix": [round(x, 4) if x != 1.0 else 1.0 for x in w],
        }
        print(
            f"{sid}: P={proj:.4f}, f_sky={f_sky:.4f} "
            f"(lit {fp.get('f_sky', '—')}), w_sum={w_sum:.0f}"
        )

    out_dir = Path(__file__).parent
    fits_files = write_fits_masks(out_dir, nside, survey_weights) if write_fits else []

    return {
        "schema_version": "1.0",
        "nside": nside,
        "npix": npix,
        "healpix_backend": "astropy-healpix",
        "toolchain_note": (
            "healpy pip wheel build failed on Win/Python 3.13 (pkgconfig None); "
            "astropy-healpix 1.1.3 ring-centre projection used — matches Scratch §5.4 "
            "proper-HEALPix validation (P_wagenveld_north=0.3234 at Nside=8 b>=0)."
        ),
        "provenance_note": (
            "Catalogue-grade LoTSS-DR2 footprint (two-region cap model) + "
            "Galactic-cut masks for CatWISE/Quaia/Singal. Symmetric Galactic cuts "
            "yield P≈0 at ring-centre; LoTSS asymmetry carries Test A leverage."
        ),
        "n_pref_l_deg": n_pref_l,
        "n_pref_b_deg": n_pref_b,
        "lotss_literature_f_sky": round(LOTSS_LITERATURE_F_SKY, 4),
        "lotss_regions_icrs": LOTSS_REGIONS_ICRS,
        "fits_masks": fits_files,
        "surveys": surveys_out,
    }


def main():
    payload = build_footprints(nside=NSIDE, write_fits=True)
    out_path = Path(__file__).with_name(f"wagenveld_sprint_footprints_nside{NSIDE}.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"Wrote {out_path}")
    if payload["fits_masks"]:
        print(f"FITS masks: {', '.join(payload['fits_masks'])}")


if __name__ == "__main__":
    main()
