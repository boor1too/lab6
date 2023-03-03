def is_palindrome(s):
    """
    This function checks whether a passed string is palindrome or not
    """
    # Convert the string to lowercase
    s = s.lower()

    # Remove non-alphanumeric characters from the string
    s = ''.join(filter(str.isalnum, s))

    # Reverse the string
    reversed_s = s[::-1]

    # Check if the string and its reversed form are the same
    return s == reversed_s


# Test the function
s1 = "A man, a plan, a canal: Panama"
print(is_palindrome(s1))  # Output: True

s2 = "race a car"
print(is_palindrome(s2))  # Output: False