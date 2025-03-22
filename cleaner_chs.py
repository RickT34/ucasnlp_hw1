from pathlib import Path
import pickle
from tqdm import tqdm

is_chinese = lambda x: "\u4e00" <= x <= "\u9fa5"

INDOR = Path('data/ppnews/')

re = []
for i, file in tqdm(enumerate(INDOR.glob('*.pkl'))):
    l = pickle.load(open(file, 'rb'))
    f = lambda x:''.join(filter(is_chinese, x))
    re+=list(map(f, l))
    

PATH = Path('data/cleaned_chs.txt')
PATH.write_text('\n'.join(re))
