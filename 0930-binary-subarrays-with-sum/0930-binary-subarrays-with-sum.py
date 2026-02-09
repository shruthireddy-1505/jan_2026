class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count=0
        l=0
        sum_goal=0
        for r in range(len(nums)):
            sum_goal+=nums[r]
            
            while sum_goal>goal:
                sum_goal-=nums[l]
                l+=1
            count+=r-l+1
        count1=0
        l1=0
        sum_goal1=0
        if goal-1==-1:
            return count
        for r in range(len(nums)):
            sum_goal1+=nums[r]
            
            while sum_goal1>goal-1:
                sum_goal1-=nums[l1]
                l1+=1
            count1+=r-l1+1
        return count-count1
                