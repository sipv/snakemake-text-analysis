#!/usr/bin/env python3

import os
import re
import sys
from collections import Counter


def count_words(text_file, words_file):
    text = open(text_file).read().lower()
    words = [w for w in re.split(r"\W+", text) if w]
    counter = Counter(words)
    with open(words_file, 'w') as fh:
        for word, count in counter.most_common():
            fh.write(f"{count:5d} {word}\n")


if __name__ == "__main__":
    count_words(sys.argv[1], sys.argv[2])
