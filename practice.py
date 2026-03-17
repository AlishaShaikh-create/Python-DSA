
nums = [1, 2, 3, 4, 5, 6]
k = 2
i = 0
count = 0
while True:
    first = nums.pop(i)
    count+=1
    nums.append(first)
    if (count == k):
        break
print(nums)    


nums = [1, 2, 3, 4, 5, 6]
k = 2
for i in range(k):
    nums.append(nums.pop(0)) 

print(nums)        


nums = [1, 2, 3, 4, 5, 6]
n = len(nums)
k = k % n
print(k)

temp = []
for i in range(k):
    temp.append(i)

for i in range(k,n):
    nums[i-k] = nums[i]

for i in range(k):
    nums[n-k+i] = temp[i]                
        
print(nums)        


def reverseArray(arr, start, end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end-=1
def reverse(arr,k):
    n = len(arr)
    k = k% n 
    reverseArray(arr,0,k-1)
    reverseArray(arr,k,n-1)
    reverseArray(arr,0,n-1)  
    return arr     
nums = [1, 2, 3, 4, 5, 6]  
k=2
print(reverse(nums,k))  