#循环列表的使用

from collections import deque

deque=deque(['1','2','2'])
deque.rotate(1)
print(deque)