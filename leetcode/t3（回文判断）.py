#判断回文

from collections import deque

words=['RADAR','WARTER START','MILK KLIM','RESERVERED','IWI','ABBA']
i=0
for word in words:
    deque = deque([])
    for c in word:
        deque.appendleft(c)
        i+=1
    print(deque)
    for c in word:
        if c==deque.popleft() and i==len(deque):

            print(word+"is huiwen")
        else:
            print(word+"not huiwen")



    deque.clear()