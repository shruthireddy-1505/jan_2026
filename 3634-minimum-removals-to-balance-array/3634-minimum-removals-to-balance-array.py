class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        max_size=0
        nums.sort()
        l=0
        for r in range(len(nums)):
            while nums[r]>k*nums[l]:
                l+=1
            max_size=max(max_size,r-l+1)
        return len(nums)-max_size