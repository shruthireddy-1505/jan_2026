class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        max_count=0
        count=0
        for r in range(len(nums)):
            while nums[r]==0 and count!=-1:
                count-=1
                l+=1
            count+=1
            max_count=max(max_count,count)
        return max_count