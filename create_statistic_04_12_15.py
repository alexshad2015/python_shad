from collections import Counter
import re
import glob
import pickle


def create_statistics_one_word():
    path = 'C:\\dickens\*.txt'
    files = glob.glob(path)
    output = Counter()
    for name in files:
        with open(name, 'r') as sample:
            input = (re.findall(r"[\w']+|[.!?]", sample.read().lower()))
            tmp = Counter(input)
            output += tmp
    with open('C:\\dickens\\stat\\all_words_2.pickle', 'w') as result:
             pickle.dump(dict(output), result)


def create_statistics_two_words():
    path = 'C:\\dickens\*.txt'
    files = glob.glob(path)
    output = Counter()
    for name in files:
        with open(name, 'r') as sample:
            input = (re.findall(r"[\w']+|[.!?]", sample.read().lower()))
            tmp = Counter(zip((input), input[1:])).copy()
            output += tmp
    with open('C:\\dickens\\stat\\stat_two_words_2.pickle', 'w') as result:
                pickle.dump(dict(output), result)


def create_statistics_three_words():
    path = 'C:\\dickens\*.txt'
    files = glob.glob(path)
    output = Counter()
    for name in files:
        with open(name, 'r') as sample:
            input = (re.findall(r"[\w']+|[.!?]", sample.read().lower()))
            tmp = Counter(zip(input, input[1:], input[2:])).copy()
            output += tmp
    with open('C:\\dickens\\stat\\stat_three_words_2.pickle', 'w') as result:
               pickle.dump(dict(output), result)


if __name__ == "__main__":
    create_statistics_one_word()     
    create_statistics_two_words()
    create_statistics_three_words()