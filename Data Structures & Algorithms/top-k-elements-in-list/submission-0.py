class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1 = Counter()
        
        for i in nums:
            hash1[i] += 1
        return [item[0] for item in hash1.most_common(k)]