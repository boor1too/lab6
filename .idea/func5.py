def all_true(t):
    return all(t)

# example usage
t1 = (True, True, False)
t2 = (True, True, True)

print(all_true(t1)) # False
print(all_true(t2)) # True