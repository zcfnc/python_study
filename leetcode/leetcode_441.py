


def arrangeCoins(n):
    i = 1

    if (n == 0):
        return 0

    while (n - i >= i + 1):
        n = n - i
        i += 1
        print(n)
    return i

n=arrangeCoins(6)
print(n)