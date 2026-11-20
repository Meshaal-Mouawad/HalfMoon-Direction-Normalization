from pathlib import Path
source = Path('Supplement.aux').read_text()
Path('Supplement_labels.aux').write_text('\\relax\n' + '\n'.join(line for line in source.splitlines() if line.startswith('\\newlabel')) + '\n')
