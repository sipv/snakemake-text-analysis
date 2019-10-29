import re
from collections import Counter


def ngrams(in_file, n, out_file):
    with open(in_file) as fh:
        text = fh.read()

    words = [w.lower() for w in re.split("\W+", text) if w]
    counter = Counter([w[i:i+n] for w in words
                       for i in range(len(w) - n + 1)])

    with open(out_file, 'w') as fh:
        for ngram, count in counter.most_common():
            fh.write(f"{count:5d} {ngram}\n")


def word_lengths(words_file, count_file):
    with open(words_file) as fh:
        lines = fh.readlines()

    word_lengths = {}
    for line in lines:
        count, word = line.strip().split()
        count = int(count)
        if len(word) not in word_lengths:
            word_lengths[len(word)] = count
        else:
            word_lengths[len(word)] += count

    with open(count_file, 'w') as fh:
        for i in range(1, max(word_lengths.keys()) + 1):
            fh.write(f"{i} {word_lengths.get(i, 0)}\n")
