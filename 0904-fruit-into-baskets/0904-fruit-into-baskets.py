class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        d={}
        l=0
        max_len=0
        for r in range(len(fruits)):
            if fruits[r] in d:
                d[fruits[r]]+=1
            else:
                d[fruits[r]]=1
            while len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len