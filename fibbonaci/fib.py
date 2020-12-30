"""
This is my first attempt at fibbonaci from memory.
I used cursors similar to how we work with linked lists.
"""


def fib_iterative(n):
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


def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_iterative(n - 1) + fib_recursive(n - 2)


memo = {0: 0, 1: 0, 2: 1}


def fib_memo(n):
    try:
        return memo[n]
    except KeyError:
        try:
            n_1 = memo[n - 1]
        except KeyError:
            n_1 = fib_memo(n - 1)
            memo[n - 1] = n_1
        try:
            n_2 = memo[n - 2]
        except KeyError:
            n_2 = fib_memo(n - 2)
            memo[n - 2] = n_2

    return n_1 + n_2


def fib_branch_prediction(n):
    if n in memo:
        return memo[n]

    if n - 1 in memo:
        n_1 = memo[n - 1]
    else:
        n_1 = fib_branch_prediction(n - 1)
        memo[n - 1] = n_1
    if n - 2 in memo:
        n_2 = memo[n - 2]
    else:
        n_2 = fib_branch_prediction(n - 2)
        memo[n - 2] = n_2

    return n_1 + n_2


# # Iterative approach
# print("Testing iterative approach on 1-20")
# for i in range(1, 20):
#     print(fib_iterative(i))
#
# # recursive
# print("Testing recursive approach on 1-20")
# for i in range(1, 20):
#     print(fib_recursive(i))
#
# # Memoization
# memo = {0: 0, 1: 0, 2: 1}
# print("Testing memoization approach on 1-20")
# for i in range(1, 20):
#     print(fib_memo(i))
#
# # Memoization with branch prediction
# memo = {0: 0, 1: 0, 2: 1}
# print("Testing branch prediction approach on 1-20")
# for i in range(1, 20):
#     print(fib_branch_prediction(i))
#
# # Timed tests
#
# ns = 950
# memo = {0: 0, 1: 0, 2: 1}
#
# fib_memo(ns)
#
# memo = {0: 0, 1: 0, 2: 1}
# fib_branch_prediction(ns)
#
# fib_iterative(ns)