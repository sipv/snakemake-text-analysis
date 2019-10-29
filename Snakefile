import util


LANGS = ["en", "fr"]
NGRAMS = [1, 2, 3]


rule all:
    input: "run/results.pdf"


rule count_words:
    input: "data/udhr.{lang}.txt"
    output: "run/words.{lang}.txt"
    shell:
        "python util/count_words.py {input} {output}"


rule word_lengths:
    input: "run/words.{lang}.txt"
    output: "run/word_lengths.{lang}.txt"
    run: util.text.word_lengths(input[0], output[0])


rule ngrams:
    input: "data/udhr.{lang}.txt"
    output: "run/ngram-{n}.{lang}.txt"
    run: util.text.ngrams(input[0], int(wildcards.n), output[0])


rule plot:
    input:
        wordlengths=expand("run/word_lengths.{lang}.txt", lang=LANGS),
        words=expand("run/words.{lang}.txt", lang=LANGS),
        ngrams=expand("run/ngram-{n}.{lang}.txt", n=NGRAMS, lang=LANGS)
    output: "run/results.pdf"
    run:
        util.plot.plot(input.wordlengths, input.words, input.ngrams,
                       NGRAMS, LANGS, output[0])
