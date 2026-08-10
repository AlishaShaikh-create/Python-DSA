def printing_1_to_N(i,n):
    if i > n:
        return
    print(i)
    i+=1
    printing_1_to_N(i,n)
    
printing_1_to_N(1,10)    