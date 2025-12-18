#hallow Rectangle


n=3
for i in range(1,n+1):
    string=""
   
    for j in range(1,n+1):
        
        if i==1 or i==n:
            string+='*'
        else:
            if j==1 or j==n:
                string+='*'
            else:
                string+=" "    
                
    print(string)        
    
n=3
for i in range(n):
   
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")       