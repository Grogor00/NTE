function Str(el)
  local map = {
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
    ["∎"] = "$\\qedhere$",
    ["❌"] = "FAIL",
    ["⚠"] = "WARN",
  }

  if map[el.text] then
    local tex = map[el.text]
    if tex:match("^\\") then
      return pandoc.RawInline("tex", "$" .. tex .. "$")
    end
    return pandoc.Str(tex)
  end

  return el
end
