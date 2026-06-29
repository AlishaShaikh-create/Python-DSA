def merge(nums1 , n, nums2 , m):
    i  = 0 
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i+=1
        else:
            nums1.insert(i,nums2[j])
            j+=1
    while j < len(nums2):
        nums1.append(nums2[j])
        j+=1

    return nums1            

nums1 = [0, 2, 7, 8]
nums2 =  [-7, -3, -1]
print(merge(nums1,4,nums2,3))


# Majority Element in the array
def Majority_Element(nums):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num,0)+1
    print(hashmap)
    
    count = 0
    ele = 0    
    for key , value in hashmap.items():
        if value > count:
            count = value
            ele = key
    return ele
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]   
print(Majority_Element(nums))  



