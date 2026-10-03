# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(r"C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Workflow\cursor_autonomous_inbound.ps1")
t = p.read_text(encoding="utf-8")

new_listen = r'''$script:NTEInboundListenPatterns = @(
  '^P0_.*\.md$'
  '^ROOT_P0_.*\.md$'
  '^CONSOLIDATED_.*\.md$'
  '^PRIORITY_.*\.md$'
  '^DIRECTIVE_.*\.md$'
  '^Directive_.*\.md$'
  '^SEED_.*\.md$'
  '^Handoff_.*\.md$'
  '^Arbitration_.*\.md$'
  '^Register_.*\.md$'
)
'''

t2, n1 = re.subn(
    r"\$script:NTEInboundListenPatterns = @\([\s\S]*?\)\r?\n",
    new_listen,
    t,
    count=1,
)

new_fn = r'''function Get-InboundPollPattern([string]$Stream) {
  switch ($Stream) {
    'main' {
      # All handoff-class artifacts — To: line is NOT a filter (Greg 2026-09-25)
      return '(?i)^((P0_|ROOT_P0_|CONSOLIDATED_|PRIORITY_|DIRECTIVE_|Directive_|SEED_|Handoff_|Arbitration_|Register_).*)\.md$'
    }
    'ac_jammer' {
      return '(?i)^((SEED_.*Jammer|Handoff_.*(AC|Jammer|Scratch|Cursor)|Directive_.*(AC|Jammer|Scratch)|Arbitration_.*).*)\.md$'
    }
    'pc_scratch' {
      return '(?i)^((Handoff_.*(PC|Scratch)|Directive_.*Scratch|Handoff_AC_to_PC|Handoff_PC_).*)\.md$'
    }
    default { return $null }
  }
}
'''

t3, n2 = re.subn(
    r"function Get-InboundPollPattern\([^\)]*\) \{[\s\S]*?\n\}\r?\n",
    new_fn,
    t2,
    count=1,
)

# Also expand Test-InboundHandoffPollCandidate for main-style inventory? Keep as-is for promote path.
# Broaden Test-InboundFileMatches already uses ListenPatterns.

p.write_text(t3, encoding="utf-8")
print(f"listen_replaced={n1} fn_replaced={n2}")
