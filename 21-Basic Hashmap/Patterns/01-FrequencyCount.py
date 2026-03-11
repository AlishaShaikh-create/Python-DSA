nums = [1,2,2,3,3,3]
freq={}
count=1
for num in nums:
    if num not in freq:
        freq[num]=count
    else:
        freq[num]+=count
print(freq)            