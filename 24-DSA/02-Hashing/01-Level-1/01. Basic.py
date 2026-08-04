# two sum 
def twoSum(nums , target):
    hashmap = {}
    # using the enumerate function

    # for key , value in enumerate(nums):
    #     complement = target - value 
    #     if complement in hashmap:
    #         return [hashmap[complement], key]
    #     hashmap[value] = key
    #     print(hashmap)  

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,target))

# Contains Duplicate 

def containsDuplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1, 2, 3]
print(containsDuplicates(nums))    

# Valid Anangram 
def ValidAnagram(s , t):
    s_hash= {}
    t_hash= {}
    for ch in s:
        if ch in s_hash:
            s_hash[ch]+=1
        else :
            s_hash[ch] =1

    for ch in t :
        if ch in t_hash:
            t_hash[ch]+=1
        else :
            t_hash[ch] = 1

    return s_hash == t_hash

   
s = "anagram"
t = "nagaram"                        
print(ValidAnagram(s, t))


        
    