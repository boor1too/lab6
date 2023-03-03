def count_upper_lower(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    return (upper_count, lower_count)

string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower(string)
print("Number of upper case letters: ", upper_count)
print("Number of lower case letters: ", lower_count)