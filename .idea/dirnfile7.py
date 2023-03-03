with open('input_file.txt', 'r') as input_file:
    with open('output_file.txt', 'w') as output_file:
        output_file.write(input_file.read())