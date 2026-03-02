def pattern(n):
    for i in range(1,n+1):
        temp=''
        for j in range(1,i+1):
            temp+=str(j)
            
        print(temp)
           

pattern(4)        