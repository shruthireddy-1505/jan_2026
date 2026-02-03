class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        min_len=float("inf")
        sum_x=0
        for r in range(len(nums)):
            sum_x+=nums[r]
            while sum_x>=target:
                min_len=min(min_len,r-l+1)
                sum_x-=nums[l]
                l+=1

        if min_len==float("inf"):
            return 0
        else:
            return min_len