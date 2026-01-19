class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_sum=sum(cardPoints[:k])
        max_sum=curr_sum
        l=len(cardPoints)-1
        r=k-1
        while l>=len(cardPoints)-k:
            curr_sum-=cardPoints[r]
            curr_sum+=cardPoints[l]
            r-=1
            l-=1
            max_sum=max(max_sum,curr_sum)
        return max_sum