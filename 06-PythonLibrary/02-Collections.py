from collections import deque
dq=deque([1,2,3])
dq.append(5) #deque([1, 2, 3, 5])
print(dq)

dq.appendleft(10)
print(dq) # deque([10, 1, 2, 3, 5])

ele=dq.pop()
print(ele) #5
print(dq) #deque([10, 1, 2, 3])

element=dq.popleft()
print(element) #10
print(dq) #deque([1, 2, 3])


dq.extend(['alisha',89])
print(dq) #deque([1, 2, 3, 'alisha', 89])

dq.extendleft(['shaikh',50])
print(dq) #deque([50, 'shaikh', 1, 2, 3, 'alisha', 89])


dq.rotate(2)
print(dq) #deque(['alisha', 89, 50, 'shaikh', 1, 2, 3])

print(len(dq)) # 7