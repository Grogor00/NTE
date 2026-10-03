-- Break long underscore- and slash-separated paths in tables so p-column cells wrap.
local function break_string(text)
  local result = {}
  local pos = 1
  while pos <= #text do
    local next_us = text:find("_", pos, true)
    local next_sl = text:find("/", pos, true)
    local next_pos = nil
    local ch = nil

    if next_us and (not next_sl or next_us <= next_sl) then
      next_pos = next_us
      ch = "_"
    elseif next_sl then
      next_pos = next_sl
      ch = "/"
    end

    if next_pos then
      if next_pos > pos then
        table.insert(result, pandoc.Str(text:sub(pos, next_pos - 1)))
      end
      table.insert(result, pandoc.Str(ch))
      table.insert(result, pandoc.RawInline("tex", "\\allowbreak{}"))
      pos = next_pos + 1
    else
      table.insert(result, pandoc.Str(text:sub(pos)))
      break
    end
  end
  return result
end

local function break_inlines(inlines)
  local result = {}
  for _, el in ipairs(inlines) do
    if el.t == "Str" and (el.text:find("_", 1, true) or el.text:find("/", 1, true)) then
      for _, part in ipairs(break_string(el.text)) do
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

  if n == 3 and (hdr:match("companion") or hdr:match("file")) then
    tbl.colspecs = {
      { tbl.colspecs[1][1], 0.24 },
      { tbl.colspecs[2][1], 0.56 },
      { tbl.colspecs[3][1], 0.20 },
    }
  elseif n == 2 and hdr:match("path") then
    tbl.colspecs = {
      { tbl.colspecs[1][1], 0.28 },
      { tbl.colspecs[2][1], 0.72 },
    }
  elseif n == 2 and hdr:match("start here") then
    tbl.colspecs = {
      { tbl.colspecs[1][1], 0.34 },
      { tbl.colspecs[2][1], 0.66 },
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
