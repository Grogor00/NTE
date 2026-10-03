"""Vendored HEALPix ring pixel centres (no healpy C extension required)."""
from __future__ import annotations

import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u


def ring_pix2ang(nside: int, ipix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return colatitude theta and longitude phi (radians) for ring-ordered pixels."""
    ipix = np.atleast_1d(np.asarray(ipix, dtype=np.int64))
    npix = 12 * nside * nside
    ncap = 2 * nside * (nside - 1)

    iring = np.zeros(ipix.shape, dtype=np.int64)
    iphi = np.zeros(ipix.shape, dtype=np.int64)

    ip = ipix.copy()

    m = ip < ncap
    if np.any(m):
        ipm = ip[m]
        iring[m] = ((1 + np.sqrt(1 + 2.0 * ipm / nside)) / 2.0).astype(np.int64)
        iphi[m] = ipm - 2 * nside * (iring[m] - 1) * iring[m]

    m = ip >= npix - ncap
    if np.any(m):
        ipm = npix - ip[m]
        iring[m] = ((1 + np.sqrt(1 + 2.0 * ipm / nside)) / 2.0).astype(np.int64)
        iphi[m] = ipm - 2 * nside * (iring[m] - 1) * iring[m]

    m = ~(ip < ncap) & ~(ip >= npix - ncap)
    if np.any(m):
        ipm = ip[m]
        iring[m] = ((ipm - ncap) // (4 * nside)) + nside
        iphi[m] = ipm - ncap - (iring[m] - nside) * 4 * nside

    north = iring <= nside
    z = np.empty_like(iring, dtype=np.float64)
    z[north] = 1.0 - (iring[north] ** 2) / (3.0 * nside ** 2)
    eq = (iring > nside) & (iring < 3 * nside)
    z[eq] = (2.0 * nside - iring[eq]) / (1.5 * nside)
    south = iring >= 3 * nside
    z[south] = (iring[south] - 3.0 * nside) ** 2 / (3.0 * nside ** 2) - 1.0

    theta = np.arccos(np.clip(z, -1.0, 1.0))
    phi = (np.pi / (2.0 * nside)) * iphi
    return theta, phi


def pix2galactic_lb(nside: int, ipix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """HEALPix ring pixel indices -> galactic l, b in degrees."""
    theta, phi = ring_pix2ang(nside, ipix)
    # HEALPix: theta colatitude from north pole; phi east longitude (ICRS-like)
    ra = phi
    dec = np.pi / 2.0 - theta
    c = SkyCoord(ra=ra * u.rad, dec=dec * u.rad, frame="icrs")
    g = c.galactic
    return g.l.deg, g.b.deg
