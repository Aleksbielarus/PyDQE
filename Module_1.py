import random


# CREATE LIST OF 100 RANDOM NUMBERS FROM 0 T0 1000
'''
    Generate list of random numbers.
        first - it's a first number from range;
        last - it's a last number from range;
        cnt - it's a count of numbers should be generated.
'''
def list_gen(first, last, cnt):
    numbers = [random.randrange(first, last) for number in range(0, cnt)]
    return numbers


# SORT LIST FROM MIN TO MAX (WITHOUT USING SORT())
'''
    This sorting based on swap numbers in required order.
    If numbers are in ascending flag swapped turn False and loop breaks.
'''
def sort_funk(lst):
    for i in range(len(lst)):
        swapped = False
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if swapped == False:
            break
    return numbers


# CALCULATE AVERAGE FOR EVEN AND ODD NUMBERS
'''
    Calculate avg add or even number from list.
        lst - list of numbers
        flag - odd or even
'''
def avg_odd_even(lst, flag):
    filtering_list = list()
    if flag == "odd":
        for number in lst:  # create list of odd numbers
            if number % 2 != 0:
                filtering_list.append(number)
    elif flag == "even":
        for number in lst:  # create list of even numbers
            if number % 2 == 0:
                filtering_list.append(number)
    avg_num = sum(filtering_list) / len(filtering_list)
    return f'Average among {flag} numbers is {avg_num}'


# execute list_gen function and save result into numbers variable
numbers = list_gen(0, 1000, 100)

# print not sorted and sorted list of values
print(numbers)
print(sort_funk(numbers))

# print avg add and even number
print(avg_odd_even(numbers, 'odd'))
print(avg_odd_even(numbers, 'even'))