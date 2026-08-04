# Counting the frequency :
def counting_frequency(nums):
    hashmap = {}
    for num in nums :
        if num in hashmap:
            hashmap[num]+=1
        else :
            hashmap[num] = 1
    return hashmap

nums = [1, 2, 2, 3, 3, 3]
print(counting_frequency(nums))