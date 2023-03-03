import os

path = input("Enter a path: ")

# Test for existence
if os.path.exists(path):
    print(f"{path} exists.")
else:
    print(f"{path} does not exist.")
    exit()

# Test for readability
if os.access(path, os.R_OK):
    print(f"{path} is readable.")
else:
    print(f"{path} is not readable.")

# Test for writability
if os.access(path, os.W_OK):
    print(f"{path} is writable.")
else:
    print(f"{path} is not writable.")

# Test for executability
if os.access(path, os.X_OK):
    print(f"{path} is executable.")
else:
    print(f"{path} is not executable.")

# Find the filename and directory portion of the path
dirname = os.path.dirname(path)
filename = os.path.basename(path)
print(f"Directory: {dirname}")
print(f"Filename: {filename}")