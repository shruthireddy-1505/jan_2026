class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_count=0
        l=0
        for i in nums:
            if i==1:
                ones_count+=1
        min_count=float("inf")
        count=0
        for i in range(ones_count):
            if nums[i]==0:
                count+=1
        min_count=count
        nums=nums+nums
        for r in range(ones_count,len(nums)):
            if nums[l]==0:
                count-=1
            if nums[r]==0:
                count+=1
            l+=1
            min_count=min(min_count,count)
        return min_count