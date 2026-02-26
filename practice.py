def printNumber(x,n):
    for i in range(n):
        print(x,end='')
        
        if i < n-1:
            print(" ", end='')
    print()
printNumber(7,4)

