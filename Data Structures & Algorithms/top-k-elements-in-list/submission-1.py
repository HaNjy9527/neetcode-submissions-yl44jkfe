class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int);

        for i in nums:
            if(res[i] is not None):
                res[i] += 1;
            else:
                res[i] = 1;
        
        return sorted(res, key = lambda x : res[x],reverse = True)[:k]

            