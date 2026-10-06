-- Sanitize YAML metadata (title, subtitle) — sanitize.lua only walks body Str nodes.
local glyph_map = {
  ["✓"] = "PASS",
  ["✔"] = "PASS",
  ["☑"] = "PASS",
  ["☒"] = "FAIL",
  ["✗"] = "FAIL",
  ["⟹"] = "=>",
  ["⟶"] = "->",
  ["⟵"] = "<-",
  ["→"] = "->",
  ["←"] = "<-",
  ["↪"] = "->",
  ["≲"] = "<~",
  ["∝"] = "\\propto",
  ["𝕆"] = "\\mathbb{O}",
  ["ℍ"] = "\\mathbb{H}",
  ["ℂ"] = "\\mathbb{C}",
  ["ℝ"] = "\\mathbb{R}",
  ["𝒜"] = "\\mathcal{A}",
  ["𝒦"] = "\\mathcal{K}",
  ["ℋ"] = "\\mathcal{H}",
  ["𝒟"] = "\\mathcal{D}",
}

local UNBREAKABLE = {
  ["(𝕆 ⊕ 𝕆)"] = "\\mbox{$(\\mathbb{O} \\oplus \\mathbb{O})$}",
}

local function map_char(ch)
  local tex = glyph_map[ch]
  if not tex then
    return { pandoc.Str(ch) }
  end
  if tex:match("^\\") then
    return { pandoc.RawInline("tex", "$" .. tex .. "$") }
  end
  return { pandoc.Str(tex) }
end

local function append_text_chars(text, out)
  for _, ch in utf8.codes(text) do
    local s = utf8.char(ch)
    for _, mapped in ipairs(map_char(s)) do
      table.insert(out, mapped)
    end
  end
end

local function protected_string_to_inlines(text)
  local out = {}
  local pos = 1
  while pos <= #text do
    local best_start, best_end, best_repl = nil, nil, nil
    for pat, repl in pairs(UNBREAKABLE) do
      local a, b = text:find(pat, pos, true)
      if a and (not best_start or a < best_start) then
        best_start, best_end, best_repl = a, b, repl
      end
    end
    if not best_start then
      append_text_chars(text:sub(pos), out)
      break
    end
    if best_start > pos then
      append_text_chars(text:sub(pos, best_start - 1), out)
    end
    table.insert(out, pandoc.RawInline("tex", best_repl))
    pos = best_end + 1
  end
  return out
end

local function meta_string(val)
  if val == nil then
    return nil
  end
  local t = pandoc.utils.type(val)
  if t == "string" then
    return val
  end
  if t == "Inlines" then
    return pandoc.utils.stringify(val)
  end
  return nil
end

local function fix_meta(val)
  if val == nil then
    return nil
  end
  local s = meta_string(val)
  if s then
    return protected_string_to_inlines(s)
  end
  return val
end

function Meta(meta)
  if meta.title then
    meta.title = fix_meta(meta.title)
  end
  if meta.subtitle then
    meta.subtitle = fix_meta(meta.subtitle)
  end
  return meta
end
