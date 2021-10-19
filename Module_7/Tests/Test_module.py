import re
import string
import csv


def write_csv(csvfile, words_dict):
    with open(csvfile, "a", newline='') as word_count:
        writer = csv.writer(word_count)
        for key, value in words_dict.items():
            writer.writerow([key, value])


def word_count(txt, csvfile):
    punctuation_list = str(['|'.join(string.punctuation)])
    non_punctuation_text = re.sub(punctuation_list, "", txt).lower().strip()
    words_dict = {}
    for word in non_punctuation_text.split(' '):
        if word in words_dict:
            n = {word: words_dict[word]+1}
            words_dict.update(n)
        elif word not in words_dict:
            n = {word: 1}
            words_dict.update(n)
    write_csv(csvfile, words_dict)
    return words_dict


def symbols_count(txt):
    pass

