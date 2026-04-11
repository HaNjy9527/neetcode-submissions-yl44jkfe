class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                l = prices[j]-prices[i];
                if(l>max):
                    max = l;


        return max;