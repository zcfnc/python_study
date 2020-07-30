

n=30
count = 0

all=1

for i in range(1, n + 1):
    if i % 5 == 0:
        count += 1
        if i / 5 % 5 ==0:
            count+=1
    all*=i

    print(i,all)
print(count)