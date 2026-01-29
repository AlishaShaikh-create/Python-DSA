# remove duplicate elements in the sorted array

def remove_duplicate(lst):
  i=0
  while i <len(lst)-1:
      if lst[i]==lst[i+1]:
          lst.remove(lst[i+1])
      else:
          i+=1
  return lst         

print(remove_duplicate([0,0,1,1,1,2,2,3,3,4]))       
        
        