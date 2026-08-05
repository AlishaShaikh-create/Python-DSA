def sumOfarray(arr):

    def helper(i, sum):
        if i > len(arr)-1:
            return sum
        sum+=arr[i]
        return helper(i+1,sum)

    return helper(0,0)

arr=[1,2,3]
print(sumOfarray(arr))