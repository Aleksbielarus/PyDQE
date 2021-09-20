import random
import string


'''
1.CREATE S LIST OF RANDOM NUMBER OF DICT (FROM 2 TO 10)
'''


# generate random number
def dict_count(first, last):
    dct_count = random.randrange(first, last + 1)
    return dct_count


def gen_dict_list():
    for dct in range(1, last):
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


'''
    2. GET PREVIOUSLY GENERATED LIST OF DICTS AND CREATE ONE COMMON DICT
'''


def split_dict_from_list(dict_list):
    # create set of keys
    all_keys = set().union(*(d.keys() for d in dict_list))
    result_dict = {}
    # keys iteration
    for key in all_keys:
        max_value = 0
        key_index = 0
        update = 0  # kostyl
        # dict iterate
        for dct in range(0, len(dict_list)):
            # keys and values iteration
            for k, v in dict_list[dct].items():
                if k == key:
                    update += 1
                    if v >= max_value:
                        key_index = dct + 1
                        max_value = v
        if update == 1:
            result_dict.update({str(key): max_value})
        elif update > 1:
            result_dict.update({str(key) + '_' + str(key_index): max_value})
    return result_dict


last = dict_count(2, 10)
dict_list = []
list_of_dicts = gen_dict_list()
print(list_of_dicts)
print(split_dict_from_list(list_of_dicts))
