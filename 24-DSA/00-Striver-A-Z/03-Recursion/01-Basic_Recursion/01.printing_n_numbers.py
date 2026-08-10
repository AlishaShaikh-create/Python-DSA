def Printing_Name(name,count , n):
    if count == n :
        return
    print(name)
    count+=1
    Printing_Name(name,count,n) 

Printing_Name("Alisha",0,3)    