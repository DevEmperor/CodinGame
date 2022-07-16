import numpy as np


def fib(n):
    Matrix = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])
    return np.matmul(Matrix ** n, vec)


nb = int(input())
for i in range(nb):
    a, b, d = [int(j) for j in input().split()]
    divident = sum(int(fib(x)[0]) for x in range(a, b + 1))
    if divident % d == 0:
        print(f"F_{a} + ... + F_{b} is divisible by {d}")
    else:
        print(f"F_{a} + ... + F_{b} is NOT divisible by {d}")
