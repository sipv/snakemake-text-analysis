
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot(word_length_files, occurences_files, ngram_files,
         ngrams, languages, img_file):

    nlangs = len(languages)

    plt.figure(figsize=(10, 3*nlangs))

    for i in range(nlangs):
        with open(word_length_files[i]) as fh:
            lines = fh.readlines()

        lens = [int(line.split()[0]) for line in lines]
        counts = [int(line.split()[1]) for line in lines]

        if i == 0:
            ax = plt.subplot2grid((nlangs, 2), (i, 0))
        else:
            plt.subplot2grid((nlangs, 2), (i, 0), sharex=ax, sharey=ax)

        plt.title("Word lengths (" + languages[i] + ")")
        plt.bar(lens, counts)
        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
        plt.xlim(left=0.2)

        with open(occurences_files[i]) as fh:
            lines = fh.readlines()

        for k in range(10):
            plt.text(0.6, 0.9 - 0.07*k, lines[k], ha='left', va='center',
                     family='monospace', transform=plt.gca().transAxes)

        plt.subplot2grid((nlangs, 2), (i, 1))
        plt.title("ngrams (" + languages[i] + ")")
        for j, n in enumerate(ngrams):
            with open(ngram_files[i + j*nlangs]) as fh:
                lines = fh.readlines()
            for k in range(10):
                plt.text(0.05 + j*0.2, 0.9 - 0.07*k, lines[k],
                         family='monospace', ha='left', va='center')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.xticks([])
        plt.yticks([])

    plt.tight_layout()
    plt.savefig(img_file)
