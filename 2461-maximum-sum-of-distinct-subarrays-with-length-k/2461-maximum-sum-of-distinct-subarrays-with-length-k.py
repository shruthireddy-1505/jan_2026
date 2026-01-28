class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        seen=set()
        curr_sum=0
        max_sum=0
        for r in range(len(nums)):
            while nums[r] in seen:
                curr_sum-=nums[l]
                seen.remove(nums[l])
                l+=1
            seen.add(nums[r])
            curr_sum+=nums[r]
            if r-l+1==k:
                max_sum=max(max_sum,curr_sum)
                curr_sum-=nums[l]
                seen.remove(nums[l])
                l+=1
        return max_sum