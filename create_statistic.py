import collections
import re
import glob
import pickle


def create_statistics_one_word():
    path = 'C:\\Users\\Alexander\\Downloads\\test\\dickens\*.txt'
    files = glob.glob(path)
    output = []
    for name in files:
        with open(name, 'r') as sample:
            input = (re.findall(r"[\w']+|[.!?]", sample.read().lower()))
            tmp = list(input)
            output += tmp
    with open('C:\\Users\\Alexander\\Downloads\\test\\ \
              dickens\\stat\\all_words.pickle', 'w') as result:
                pickle.dump(output, result)


def create_statistics_two_words():
    path = 'C:\\Users\\Alexander\\Downloads\\test\\dickens\*.txt'
    files = glob.glob(path)
    output = {}
    for name in files:
        with open(name, 'r') as sample:
            input = (re.findall(r"[\w']+|[.!?]", sample.read().lower()))
            tmp = collections.Counter(zip((input), input[1:])).copy()
            output.update(tmp)
    with open('C:\\Users\\Alexander\\Downloads\\test\\ \
               dickens\\stat\\stat_two_words.pickle', 'w') as result:
                pickle.dump(output, result)


def create_statistics_three_words():
    path = 'C:\\Users\\Alexander\\Downloads\\test\\dickens\*.txt'
    files = glob.glob(path)
    output = {}
    for name in files:
        with open(name, 'r') as sample:
            input = (re.findall(r"[\w']+|[.!?]", sample.read().lower()))
            tmp = collections.Counter(zip(input, input[1:], input[2:])).copy()
            output.update(tmp)
    with open('C:\\Users\\Alexander\\Downloads\\test\\ \
               dickens\\stat\\stat_three_words.pickle', 'w') as result:
                pickle.dump(output, result)


if __name__ == "__main__":
    create_statistics_one_word()
    create_statistics_two_words()
    create_statistics_three_words()
