class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l=0
            freq={}
            d=0
            c=0
            for r in range(len(nums)):
                if nums[r] not in freq:
                    freq[nums[r]]=0
                if freq[nums[r]]==0:
                    d+=1
                freq[nums[r]]+=1

                while d>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        d-=1
                    l+=1
                c+=r-l+1
            return c
        return atmost(k)-atmost(k-1)