
def countPrimes(n):
    boon = [1] * n
    count = 0
    for i in range(2, n):
        j = 2
        while (j < n and boon[i]!=0):
            if i % j == 0 and i / j != 1:
                boon[i] = 0
                count += 1
            j += 1

    print(boon)
    print(n-count-2)


countPrimes(10000)

