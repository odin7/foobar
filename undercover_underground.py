'''
Undercover underground
======================

As you help the rabbits establish more and more resistance groups to fight against Professor Boolean, you need a way to pass messages back and forth.

Luckily there are abandoned tunnels between the warrens of the rabbits, and you need to find the best way to use them. In some cases, Beta Rabbit wants a high level of interconnectedness, especially when the groups show their loyalty and worthiness. In other scenarios the groups should be less intertwined, in case any are compromised by enemy agents or zombits.

Every warren must be connected to every other warren somehow, and no two warrens should ever have more than one tunnel between them. Your assignment: count the number of ways to connect the resistance warrens.

For example, with 3 warrens (denoted A, B, C) and 2 tunnels, there are three distinct ways to connect them:

A-B-C
A-C-B
C-A-B

With 4 warrens and 6 tunnels, the only way to connect them is to connect each warren to every other warren.

Write a function answer(N, K) which returns the number of ways to connect N distinctly labelled warrens with exactly K tunnels, so that there is a path between any two warrens.

The return value must be a string representation of the total number of ways to do so, in base 10.
N will be at least 2 and at most 20.
K will be at least one less than N and at most (N * (N - 1)) / 2

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) N = 2
    (int) K = 1
Output:
    (string) "1"

Inputs:
    (int) N = 4
    (int) K = 3
Output:
    (string) "16"
'''


from functools import wraps


def memo(func):
    # a wrapper to cache function's results
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def choose(N, k):
    if k < 0 or k > N:
        return 0
    if k == 0 or k == N:
        return 1
    k = min(k, N - k)
    c = 1
    for i in range(k):
        c = c * (N - i) // (i + 1)
    return c


@memo
def answer(N, K):
    # Number of labeled, simply connected graphs with N vertices and K edges
    # http://math.stackexchange.com/questions/689526
    max_edges = N * (N - 1) // 2  # # of all possible edges
    if K < N - 1 or K > max_edges:  # too many or too little edges
        res = 0
    elif K == N - 1:  # https://en.wikipedia.org/wiki/Cayley%27s_formula
        res = int(N ** (N - 2))
    else:
        res = choose(max_edges, K)  # all possible graphs on K edges
        for m in range(0, N - 1):
            lb = max(0, K - (m + 1) * m // 2)
            total_edges = (N - 1 - m) * (N - 2 - m) // 2
            res -= choose(N - 1, m) * sum(choose(total_edges, p) *
                                          answer(m + 1, K - p) for p in range(lb, K - m + 1))
    return res


if __name__ == '__main__':
    print(answer(20, 150))
