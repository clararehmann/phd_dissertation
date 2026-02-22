# This script cleans refs.bib by removing all 'keywords' and 'file' fields, even if split across lines.
import re

input_path = 'refs.bib'
output_path = 'refs_cleaned.bib'

with open(input_path, 'r') as infile:
    lines = infile.readlines()

cleaned_lines = []
skip = False
for line in lines:
    # Remove lines starting with keywords or file (allow whitespace)
    if re.match(r'\s*(keywords|file)\s*=.*', line):
        skip = False
        continue
    # Remove lines that are part of a multi-line file or keywords field
    if skip:
        if '},' in line or '},\n' in line or '},' in line.strip():
            skip = False
        continue
    if re.match(r'\s*(keywords|file)\s*=\s*\{.*', line) and not line.strip().endswith('},'):
        skip = True
        continue
    cleaned_lines.append(line)

with open(output_path, 'w') as outfile:
    outfile.writelines(cleaned_lines)

print('refs_cleaned.bib created. Replace refs.bib with this file if satisfied.')
