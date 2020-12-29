"""
This is my first attempt at fibbonaci from memory.
I used cursors similar to how we work with linked lists.
"""


def fibbonaci(n):
    prevprev = 0
    prev = 1
    curr = 0

    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    # algorithm
    for i in range(2, n):
        curr = prev + prevprev
        prevprev = prev
        prev = curr
    return curr


for i in range(1, 20):
    print(fibbonaci(i))
