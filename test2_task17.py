dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 =  {'key1': 1, 'key2': 2}
for i in dict1.items():
    for j in dict2.items():
        if i ==j:
            print(i)