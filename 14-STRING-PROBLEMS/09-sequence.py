# def sequence(s,t):
#     s1=[]
#     t1=[]
#     for char in s:
#         s1.append(char)
#     print("s1=",s1)
    
#     for char in t:
#         t1.append(char)    
#     print("t1=",t1)
    
#     for i in range(len(s1)):
#         if s1[i] not in t1:
#             s1.pop(i)
#             print(s1)
         
            
#     for i in range( len (s1)):
#         for j in range(len(t1)):
#             if i==j and s1[i]==t1[j]:
#                 return True
#             else:
#                 return False
                 
# print(sequence("abcde","ace"))


def sequence(s, t):
    j = 0  # pointer for t
    
    for char in s:
        if j < len(t) and char == t[j]:
            j += 1
    
    return j == len(t)

print(sequence("abcde", "ace"))
