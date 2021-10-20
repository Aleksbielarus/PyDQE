dict1 = {1:'news', 2: 'private ad', 3: 'weather', 0: 'exit'}
if int(flag) not in dict1.keys():
    print('error')
elif int(flag) in dict1.keys():
    input_note('m', flag, dict1[flag])


238