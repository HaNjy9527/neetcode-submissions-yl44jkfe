class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
    
        # 2. 依 value（頻率）降序排序，取 key（數字）
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]