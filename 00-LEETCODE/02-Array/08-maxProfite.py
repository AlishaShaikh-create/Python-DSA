def maxProfite(price):
    n=len(price)
    max_profite=0
    for i in range(n):
        for j in range(i+1,n):
            profite=price[j]-price[i]
            if profite > max_profite:
                max_profite=profite
    return max_profite

price=[7,1,5,3,6,4]
print(maxProfite(price))               


def maxProfite(price):
    min_price=price[0]
    max_profite=0
    for i in range(1,len(price)):
        profite=price[i]-min_price
        
        if profite>max_profite:
            max_profite=profite
        
        if price[i]<min_price:
            min_price=price[i]
    return max_profite            
        
price=[7,1,5,3,6,4]
print(maxProfite(price))               
    