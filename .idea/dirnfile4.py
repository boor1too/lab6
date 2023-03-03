file_name = input("Enter file name: ")

# Open the file in read mode
with open(file_name, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

# Split the contents of the file by newline characters
# and count the number of resulting lines
num_lines = len(file_contents.split('\n'))

# Print the number of lines in the file
print("The file has", num_lines, "lines.")