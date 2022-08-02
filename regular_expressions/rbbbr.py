import re

text = input('Input your text:\n')
pattern = r'[Rr]{1}[Bb]+r{1}'
match = re.findall(pattern, text)
if match:
    print(match)
else:
    print('Pattern not found')
