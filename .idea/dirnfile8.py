import os

file_path = input("Enter the file path: ")

# Check if the file exists
if not os.path.exists(file_path):
    print(f"The file {file_path} does not exist.")
    exit()

# Check if the user has permission to delete the file
if not os.access(file_path, os.W_OK):
    print(f"You do not have permission to delete the file {file_path}.")
    exit()

# Delete the file
os.remove(file_path)
print(f"The file {file_path} has been deleted.")