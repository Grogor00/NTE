-- Allow line breaks after hyphens and slashes in table cells (hyphenat is off).
local function break_string(text, chars)
  local result = {}
  local pos = 1
  while pos <= #text do
    local best = nil
    local bestch = nil
    for _, ch in ipairs(chars) do
      local p = text:find(ch, pos, true)
      if p and (not best or p < best) then
        best = p
        bestch = ch
      end
    end
    if best then
      if best > pos then
        table.insert(result, pandoc.Str(text:sub(pos, best - 1)))
      end
      table.insert(result, pandoc.Str(bestch))
      table.insert(result, pandoc.RawInline("tex", "\\allowbreak{}"))
      pos = best + 1
    else
      table.insert(result, pandoc.Str(text:sub(pos)))
      break
    end
  end
  return result
end

local BREAK_CHARS = { "-", "/" }

local function needs_break(text)
  for _, ch in ipairs(BREAK_CHARS) do
    if text:find(ch, 1, true) then
      return true
    end
  end
  return false
end

local function break_inlines(inlines)
  local result = {}
  for _, el in ipairs(inlines) do
    if el.t == "Str" and needs_break(el.text) then
      for _, part in ipairs(break_string(el.text, BREAK_CHARS)) do
        table.insert(result, part)
      end
    elseif el.content then
      el.content = break_inlines(el.content)
      table.insert(result, el)
    else
      table.insert(result, el)
    end
  end
  return result
end

local function walk_blocks(blocks)
  return pandoc.walk_block(pandoc.Div(blocks), {
    Plain = function(el)
      el.content = break_inlines(el.content)
      return el
    end,
    Para = function(el)
      el.content = break_inlines(el.content)
      return el
    end,
  }).content
end

local function header_text(tbl)
  if not tbl.head or not tbl.head.rows or #tbl.head.rows == 0 then
    return ""
  end
  local parts = {}
  for _, cell in ipairs(tbl.head.rows[1].cells) do
    table.insert(parts, pandoc.utils.stringify(cell.contents))
  end
  return table.concat(parts, " "):lower()
end

local function process_rows(rows)
  for _, row in ipairs(rows) do
    for _, cell in ipairs(row.cells) do
      cell.contents = walk_blocks(cell.contents)
    end
  end
end

function Table(tbl)
  local hdr = header_text(tbl)
  local n = #tbl.colspecs

  if n == 6 and hdr:match("approach") and hdr:match("z_2 acts on") then
    tbl.colspecs = {
      { tbl.colspecs[1][1], 0.21 },
      { tbl.colspecs[2][1], 0.19 },
      { tbl.colspecs[3][1], 0.09 },
      { tbl.colspecs[4][1], 0.13 },
      { tbl.colspecs[5][1], 0.19 },
      { tbl.colspecs[6][1], 0.19 },
    }
  end

  if tbl.head and tbl.head.rows then
    process_rows(tbl.head.rows)
  end
  for _, body in ipairs(tbl.bodies) do
    if body.body then
      process_rows(body.body)
    end
  end
  if tbl.foot and tbl.foot.rows then
    process_rows(tbl.foot.rows)
  end

  return tbl
end
