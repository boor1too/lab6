import os

path = input("Enter path to list directories and files: ")

# List only directories
print("Directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

# List only files
print("\nFiles:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

# List all directories and files
print("\nAll directories and files:")
for name in os.listdir(path):
    print(name)