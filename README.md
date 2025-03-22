# UCAS Natural Language Processing Homework 1

This is the solution of the first homework of 2025 UCAS Natural Language Processing.

## Files

- `arxivpapers.py`: Python script to download and parse arXiv papers from [arXiv](https://arxiv.org/).
- `ppnews.py`: Python script to download and parse People's Daily News articles from [PDN](http://paper.people.com.cn/rmrb/pc/layout/202503/19/node_01.htmll).
- `cleaner_chs.py`: Python script to clean Chinese text.
- `cleaner_eng.py`: Python script to clean English text.
- `experiment.py`: Python script to calculate the entropy of a dataset.
- `data_exploer.ipynb`: Jupyter notebook to plot the data.

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

Create a `data` directory under the project root directory.

1. Get the raw text data from arXiv and PDN.

```bash
python arxivpapers.py
python ppnews.py
```

2. Clean the text data.

```bash
python cleaner_chs.py
python cleaner_eng.py
```

3. Calculate the entropy of the dataset.

```bash
python experiments.py data/cleaned_eng.txt
python experiments.py data/cleaned_chs.txt
```

4. Plot the data using `data_exploer.ipynb`.

