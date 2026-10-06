﻿import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
book = pathlib.Path(r'C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book')
t = (book/'Chapter_11_What_the_Universe_Sounds_Like_v4.md').read_text(encoding='utf-8')
for m in re.finditer(r'.{0,20}[Gg]auge-birth.{0,220}', t):
  print('---')
  print(m.group(0).replace('\n',' / '))
print('temporal circle', t.count('temporal circle'))
print('single relation', t.count('single relation'))
print('circle size', t.count("circle's size"))
print('fixes the circle', t.count('fixes the circle'))
print('set by the same', t.count('set by the same'))

t10 = (book/'Chapter_10_The_Silvered_Boundary_v9.md').read_text(encoding='utf-8')
print('Ch10 coherence length', t10.count('coherence length'))
print('Ch10 coherence mass', t10.count('coherence mass'))
print('Ch10 megaparsec', t10.lower().count('megaparsec'))
for m in re.finditer(r'.{0,40}coherence length.{0,50}', t10):
  print('CL:', m.group(0).replace('\n',' '))

t9 = (book/'Chapter_09_The_Number_That_Could_Have_Failed_v5.md').read_text(encoding='utf-8')
for o in [
 'proper time crystallised',
 'The difference is 0.12, which is about 0.83',
 'joins the maximal CP phase and the maximal atmospheric angle in the strictest zero-parameter tier, with the spectral index',
]:
  print('Ch9', t9.count(o), o[:60])

tc = (book/'Appendix_C_The_Open_Ledger_v1_6_DRAFT_PC_20260925.md').read_text(encoding='utf-8')
i = tc.find('Until it closes')
print('AF3:', repr(tc[i:i+110]))

t6 = (book/'Chapter_06_Why_Quantum_Mechanics_is_Geometry_v7.md').read_text(encoding='utf-8')
for n in ['What the Reformulation Says','What the Derivation Says','The Born rule is the derived leg','The Born rule is the leg the framework has reformulated','Chapter 6 derives the probability','Chapter 6 recasts the probability','the climactic geometric chapter','the chapter where the geometric apparatus is complete']:
  print('Ch6', t6.count(n), n)

# Ch13 Q1 still present?
t13 = (book/'Chapter_13_The_Strange_Silence_of_the_Cosmological_Constant_v6.md').read_text(encoding='utf-8')
print('Ch13 tenth of a milligram', t13.count('tenth of a milligram'))
print('Ch13 twenty-two micrograms', t13.count('twenty-two micrograms'))
print('Ch13 zero proper time', t13.count('zero proper time'))
