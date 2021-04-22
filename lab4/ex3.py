import re
import itertools


def word_count(given_word, path):
    count = 0
    with open(path, 'r') as file:
        for word in parse_words(file):
            if given_word == word:
                count += 1
    return count


def clean(line):
    return re.sub(r"[,\.\'\"\(\)\-]", " ", line.strip().lower())


def parse_words(f):
    cleaned = (clean(line) for line in f)
    words_splitted = (line.split() for line in cleaned)
    words = itertools.chain.from_iterable(words_splitted)
    return words


if __name__ == '__main__':
    print(word_count('project', 'pg100.txt'))
