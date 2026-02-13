class Solution:
    def numberOfSubstrings(self, nums: str) -> int:
        freq={}
        dis=0
        count=0
        l=0
        for r in range(len(nums)):
            if nums[r] not in freq:
                freq[nums[r]]=0
            if freq[nums[r]]==0:
                dis+=1
            freq[nums[r]]+=1
            while dis==3:
                count+=len(nums)-r
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    dis-=1
                l+=1
        return count