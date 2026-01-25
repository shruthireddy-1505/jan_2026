class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        curr_sum=sum(arr[:k])
        count=0
        if curr_sum//k>=threshold:
            count+=1
        for r in range(k,len(arr)):
            curr_sum-=arr[l]
            curr_sum+=arr[r]
            if curr_sum//k>=threshold:
                count+=1
            l+=1
        return count
                