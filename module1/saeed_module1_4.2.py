# This module generates a Fibonacci sequence based on the current minute of the hour.
# The length of the sequence is twice the current minute value.
# For example, if the current minute is 15, the sequence will have 30 terms.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq

def get_fibonacci_based_on_minute():
    minute = datetime.now().minute
    n = 2 * minute
    seq = fibonacci(n)
    print(f"Fibonacci sequence for 2 * current minute ({minute}) = {n} terms:")
    print(seq)
    return seq
from datetime import datetime



# note: To test this code, simply run the module. It will print the Fibonacci sequence based on the current minute.
