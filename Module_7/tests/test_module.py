import re
import string
import csv


def write_csv(csvfile, words_dict, note_type, datetime):
    with open(csvfile, "a", newline='') as word_count:
        writer = csv.writer(word_count)
        for key, value in words_dict.items():
            writer.writerow([key, value, note_type, datetime])


def write_csv1(csvfile, words_dict, note_type, datetime):
    # headerList = ['letter', 'count_all', 'count_uppercase', 'percentage', 'note_type', 'datetime']
    with open(csvfile, "a", newline='') as word_count:
        writer = csv.writer(word_count)
        for key, value in words_dict.items():
            writer.writerow([key, value[0], value[1], value[2], note_type, datetime])


def word_count(txt, csvfile, note_type, datetime):
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
    write_csv(csvfile, words_dict, note_type, datetime)
    return words_dict


def letter_count(txt, csvfile, note_type, datetime):
    punctuation_list = str(['|'.join(string.punctuation + string.whitespace + string.digits)])
    non_punctuation_text = re.sub(punctuation_list, "", txt).strip()
    letter_dict = {}
    for letter in non_punctuation_text:
        if letter.lower() in letter_dict:
            if letter in string.ascii_uppercase:
                letter = letter.lower()
                n = {letter: [letter_dict[letter][0]+1,
                              letter_dict[letter][1]+1,
                              round((letter_dict[letter][1]+1) / (letter_dict[letter][0]+1) * 100, 2)]}
            else:
                n = {letter: [letter_dict[letter][0]+1,
                              letter_dict[letter][1],
                              round(letter_dict[letter][1] / (letter_dict[letter][0]+1) * 100, 2)]}
            letter_dict.update(n)
            pass
        elif letter.lower() not in letter_dict:
            if letter in string.ascii_uppercase:
                n = {letter.lower(): [1, 1, 100]}
            else:
                n = {letter.lower(): [1, 0, 0]}
            letter_dict.update(n)
    write_csv1(csvfile, letter_dict, note_type, datetime)
    return letter_dict






