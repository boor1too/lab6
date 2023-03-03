my_list = ['apple', 'banana', 'orange']

with open('my_file.txt', 'w') as f:
    for item in my_list:
        f.write("%s\n" % item)