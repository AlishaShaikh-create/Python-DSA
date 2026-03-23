
        
nums1 = [1,2,5]
nums2 = [ 2]
def intersection(num1,num2):
    i = 0
    j = 0
    result =[]
    while i < len(num1) and j < len(num2):
        if num1[i] == num2[j]:
            if not result or result[-1]!=num1[i]:
                result.append(num1[i])
            i+=1
            j+=1    
        elif num1[i]<num2[j]:
            i+=1
        else:
            j+=1    
    return result
print(intersection(nums1,nums2))                                                         
                                                         

            
    