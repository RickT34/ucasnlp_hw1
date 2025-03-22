from curses.ascii import isalpha
from pathlib import Path
from tqdm import tqdm

INDOR = Path('data/arxivpapers/')

re = []
for i, file in enumerate(tqdm(list(INDOR.glob('*.txt')))):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        re.append(''.join(filter(isalpha, text)))
        
PATH = Path('data/cleaned_eng.txt')
PATH.write_text('\n'.join(re))
PATH = Path('data/cleaned_eng_lower.txt')
PATH.write_text('\n'.join(re).lower())