import numpy as np
from pathlib import Path
import argparse
import tqdm

RNG = np.random.default_rng()

class Dataset:
    def __init__(self, path:Path):
        texts = path.read_text(encoding='utf-8').split('\n')
        
        vocab = list(set(''.join(texts)))
        vocab.sort()
        self.vocab2id = {char:i for i, char in enumerate(vocab)}
        self.id2vocab = vocab
        self.texts = list(map(
            lambda x: np.array(list(map(
                lambda y: self.vocab2id[y], 
                x
                )), dtype=int), 
            texts
            ))
        self.text = np.concatenate(self.texts)
    
    def shuffle(self):
       RNG.shuffle(self.texts)
       self.text = np.concatenate(self.texts)

    @property
    def vocab_size(self):
        return len(self.vocab2id)
    
def entropy(p:np.ndarray):
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

def run_sample(dataset:Dataset, window:int):
    re = np.zeros((dataset.text.shape[0]+window-1)//window)
    p = np.zeros(dataset.vocab_size, dtype=int)
    for i in range(0, len(dataset.text), window):
        end_idx = min(i+window, len(dataset.text))
        p += np.bincount(dataset.text[i:end_idx], minlength=dataset.vocab_size)
        re[i//window] = entropy(p/end_idx)
    return re
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to the cleaned text file')
    parser.add_argument('--window', type=int, default=100000, help='Window size for the entropy calculation')
    parser.add_argument('--n_samples', type=int, default=1000, help='Number of samples to generate')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    args = parser.parse_args()

    RNG = np.random.default_rng(args.seed)

    print(f'Loading dataset from {args.path}')
    dataset = Dataset(Path(args.path))
    print(f'Dataset loaded with {dataset.vocab_size} unique characters, length {len(dataset.text)}')
    
    res = []
    
    for i in tqdm.tqdm(range(args.n_samples)):
        if i != 0:
            dataset.shuffle()
        re = run_sample(dataset, args.window)
        res.append(re)
    
    res = np.array(res)
    np.save(f'{args.path}.entropy.{args.window}.{args.n_samples}.npy', res)
    

