nums = [2,4,1,5]
sum = 0
prefix_sum =[]
for i in range(len(nums)):
    sum+=nums[i]
    prefix_sum.append(sum)

print(prefix_sum)

def range_query(nums, L,R):
    prefix_sum = []
    running_sum =0
    for num in nums:
        running_sum+=num
        prefix_sum.append(running_sum)

    if L == 0:
        return prefix_sum[R]    

    return prefix_sum[R]-prefix_sum[L - 1]

nums = [2, 4, 1, 5, 3]
L = 1
R = 3  
print(range_query(nums,L,R))  


# Brute force approach
def sum_k(nums,k):
    count = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i,len(nums)):
            current_sum+=nums[j]

            if current_sum==k:
                count+=1
    return count

nums = [1,2,3]
k = 3
print(sum_k(nums,k))

def sum_k(nums,k):
    hashmap = {0:1}
    count = 0
    prefix = 0
    for  num in nums:
        prefix+=num

        needed = prefix - k
        if needed in hashmap:
            count +=hashmap[needed]
        hashmap[prefix] = hashmap.get(prefix,0)+1
        print(hashmap)
    return count        

def sum_k(nums):
    hashmap = {0:1}
    count = 0
    prefix = 0
    for  num in nums:
        prefix+=num

        needed = prefix 
        if needed in hashmap:
            count +=hashmap[needed]
        hashmap[prefix] = hashmap.get(prefix,0)+1
        # print(hashmap)
    return count            


nums = [1, -1, 2, -2]
print(sum_k(nums))

def longest_sub_array(nums,k):
    max_length = 0
    hashmap = {0:-1}
    prefix = 0

    for i in range(len(nums)):
        prefix+=nums[i]

        needed = prefix - k
        if needed in hashmap:
            length = i - hashmap[needed]
            max_length = max(length,max_length)
        if prefix not in hashmap:    
            hashmap[prefix] = i
    return max_length
nums = [1, -1, 5, -2, 3]
k = 3        
print(longest_sub_array(nums,k))