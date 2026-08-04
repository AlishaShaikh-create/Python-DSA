def printing_n_to_1(n,i):
    if n < i :
        return
    print(n)
    n-=1
    printing_n_to_1(n,i)



printing_n_to_1(10,2)

