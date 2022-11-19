class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            x=''.join(sorted(s))
            if x in d:
                d[x]=d[x]+[s]
            else:
                d[x]=[s]
        return list(d.values())
                
