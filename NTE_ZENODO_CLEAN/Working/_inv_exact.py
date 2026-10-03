﻿import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
book = pathlib.Path(r'C:\Users\gregw\My Drive\NTE_ZENODO_CLEAN\Book')
t = (book/'Chapter_11_What_the_Universe_Sounds_Like_v4.md').read_text(encoding='utf-8')
i = t.find('- **The gauge-birth temperature.**')
print('AS1 LIVE OLD:')
print(repr(t[i:i+280]))
print('---')
# second claim
i2 = t.find("The gauge-birth temperature is not an independent number")
print('SECOND T_GB claim:')
print(repr(t[i2:i2+200]))

# Ch9 exact T1 line
t9 = (book/'Chapter_09_The_Number_That_Could_Have_Failed_v5.md').read_text(encoding='utf-8')
i = t9.find('At the gauge birth')
print('\\nT1 LIVE:')
print(repr(t9[i:i+220]))
i = t9.find('Side-by-side. The framework')
print('\\nT2 LIVE:')
print(repr(t9[i:i+280]))
i = t9.find('Chapter 15 catalogues the framework')
print('\\nT3 LIVE:')
print(repr(t9[i:i+320]))

# Ch17 exact AG lines
t17 = (book/'Chapter_17_The_Working_Bet_v3.md').read_text(encoding='utf-8')
for label, needle in [
 ('AG1','The book began with a fact'),
 ('AG2','The argument, in brief'),
 ('AG3','Time from expansion'),
 ('AG4','kinetic normalisation K'),
 ('AG5','one promoted when its derivation closed'),
 ('AG6','Massive matter accumulates proper time'),
]:
  i = t17.find(needle)
  print(f'\\n{label} LIVE idx={i}:')
  print(repr(t17[max(0,i-5):i+180].replace('\n',' ')))
