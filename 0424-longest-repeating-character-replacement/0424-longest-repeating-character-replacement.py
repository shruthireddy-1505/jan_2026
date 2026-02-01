class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        max_len=0
        for r in range(len(s)):
            if s[r] in d:
                d[s[r]]+=1
            else:
                d[s[r]]=1
            max_val=max(d.values())
            while abs(max_val-(r-l+1))>k:
                d[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
            