def printing_Subsequence(index , arr , current):
    if index >= len(arr):
        print(current)
        return 

    # Take the element 
    current.append(arr[index])
    printing_Subsequence(index+1 , arr , current)

    # Back Tracking 
    current.pop()

    # Do not take the element 
    printing_Subsequence(index+1 , arr, current)

printing_Subsequence(0,[1,2,3],[])    

