import time
import math

def compute_sqrt(num, delay):
    time.sleep(delay/1000)
    return math.sqrt(num)

num = int(input("Enter a number to find the square root of: "))
delay = int(input("Enter the delay in milliseconds: "))

result = compute_sqrt(num, delay)

print(f"Square root of {num} after {delay} milliseconds is {result}")