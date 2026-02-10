class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        count=0
        odd_count=0
        for r in range(len(nums)):
            if nums[r]%2!=0:
                odd_count+=1
            while odd_count>k:
                if nums[l]%2!=0:
                    odd_count-=1
                l+=1
            count+=r-l+1
        l1=0
        count1=0
        odd_count1=0
        for r in range(len(nums)):
            if nums[r]%2!=0:
                odd_count1+=1
            while odd_count1>k-1:
                if nums[l1]%2!=0:
                    odd_count1-=1
                l1+=1
            count1+=r-l1+1
        return count-count1     