# Group Anagram
def ValidAnagram(strs):
    hashmap ={}
    # My code 
    # for ch in strs:
        
        # key = "".join(sorted(ch))
        # if key in hashmap:
        #     hashmap[key].append(ch)
        
        # else :
        #     hashmap[key] = [ch]
    
    # Optimal approach :
    for words in strs :

        count =[0]*26
        for ch in words:
            index = ord(ch) - ord('a')
            count[index]+=1
        key = tuple(count)
        if key in hashmap:
            hashmap[key].append(words)
        else :
            hashmap[key] = [words]
    print(hashmap) 
    result = []               
    for value in hashmap.values():
        result.append(value)
    print(result)    
        
   

strs = ["eat","tea","tan","ate","nat","bat"]
ValidAnagram(strs)


# Longest Consecutive Numbers 
def longestConsecutive(nums):
    seen = set(nums)
    longest = 0
    for num in  seen:
        if num -1 not in seen :
            curr_number = num
            curr_length = 1
            while curr_number+1 in seen:
                curr_number +=1
                curr_length+=1
            longest = max(curr_length, longest)
    return longest       

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))        


print("---------------------------------------")
# First Unique Character in a String
def uniqueCharacter(nums):
    ele = -1
    hashmap ={}
    for num in nums:
        if num in hashmap:
            hashmap[num]+=1
        else :
            hashmap[num]=1
    for key, value in hashmap.items():
        if value == 1:
            ele = key
            break
     
    for i in range(len(nums)):
        if ele == nums[i]:
            return i
    return ele

nums= "loveleetcode"  
print(uniqueCharacter(nums))
nums = "leetcode"      
print(uniqueCharacter(nums))
nums = "aabb"      
print(uniqueCharacter(nums))      


