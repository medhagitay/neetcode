class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*128
        for i in s:
            a[ord(i)]+=1
        for i in t:
            a[ord(i)]-=1
        for i in a:
            if i!=0:
                return False
        return True
#         d={}
#         for i in s:
#             if i in d:
#                 d[i]+=1
#             else:
#                 d[i]=1
#         for j in t:
#             if j in d:
#                 d[j]-=1
#             else:
#                 d[j]=1
        
#         for i in d:
#             if d[i]!=0:
#                 return False
#         return True
