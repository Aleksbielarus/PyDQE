import random

def list_gen(first, last, cnt):
    numbers = list()
    for i in range(0, cnt):
        # number = random.randrange(first, last)
        # numbers.append(number)
        numbers = [random.randrange(first, last) for number in range(0, cnt)]
    return numbers

numbers = list_gen(0, 1000, 100)
print(numbers)