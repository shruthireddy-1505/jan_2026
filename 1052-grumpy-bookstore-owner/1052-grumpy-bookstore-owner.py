class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                ans+=customers[i]
        res=0
        max_sum=0
        for i in range(minutes):
            if grumpy[i]==1:
                res+=customers[i]
        max_sum=res
        l=0
        for r in range(minutes,len(customers)):
            if grumpy[l]==1:
                res-=customers[l]
            if grumpy[r]==1:
                res+=customers[r]
            l+=1
            max_sum=max(max_sum,res)
        return max_sum+ans