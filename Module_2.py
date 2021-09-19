'''
1.CREATE S LIST OF RANDOM NUMBER OF DICT (FROM 2 TO 10)
'''

import random
import string


# generate random number

def dict_count(first, last):
    dct_count = random.randrange(first, last + 1)
    return dct_count


def gen_dict_list():
    for dict in range(1, last):
        dictionary = {}
        dict_len = random.randrange(len(string.ascii_lowercase))
        for i in range(1, dict_len + 1):
            key = random.choice(string.ascii_lowercase)
            value = random.randrange(0, 101)
            while key in dictionary:
                key = random.choice(string.ascii_lowercase)
            dictionary[key] = value
        # update dict_list with new dictionary
        dict_list.append(dictionary)
    return dict_list


def split_dict_from_list(dict_list):
    # create list of keys
    all_keys = set().union(*(d.keys() for d in list_of_dicts))
    result_dict = {}
    # keys iteration
    for i in all_keys:
        max_value = 0
        key_index = 0
        update = 0  # kostylz
        # dict iterate
        for dict in range (0, len(dict_list)):
            # keys and values iteration
            for k, v in dict_list[dict].items():
                if k == i:
                    update += 1
                    if v >= max_value:
                        key_index = dict + 1
                        max_value = v
        if update == 1:
            result_dict.update({str(i): max_value})
        elif update > 1:
            result_dict.update({str(i) + '_' + str(key_index): max_value})
    return result_dict


last = dict_count(2,10)
dict_list = []
list_of_dicts = gen_dict_list()
print(split_dict_from_list(list_of_dicts))