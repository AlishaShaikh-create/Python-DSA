s=["flight", "flow", "flower"]
s.sort()
print(s)

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort()
#         length=len(strs)
#         s=""
#         i=0
#         while i < len(strs[0]):
#             if strs[0][i]==strs[length-1][i]:
#                 s+=strs[0][i]
#             else:
#                 break
#             i+=1
#         return s            

