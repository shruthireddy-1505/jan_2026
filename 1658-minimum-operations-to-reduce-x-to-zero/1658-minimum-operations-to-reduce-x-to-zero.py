class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l=0
        total_sum=sum(nums)
        max_len=-1
        if total_sum<x:
            return -1
        goal=total_sum-x
        curr_sum=0
        for r in range(len(nums)):
            curr_sum+=nums[r]
            
            while curr_sum>goal:
                curr_sum-=nums[l]
                l+=1
            if curr_sum==goal:
                max_len=max(max_len,r-l+1)
        if max_len!=-1:
            return len(nums)-max_len
        else:
            return max_len