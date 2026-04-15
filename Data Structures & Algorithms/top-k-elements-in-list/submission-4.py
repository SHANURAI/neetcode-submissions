class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []
        for element in nums:
            nums_hash[element] += 1
        for key, value in nums_hash.items():
            buckets[value].append(key)
            
        for i in range(len(buckets) - 1, 0, -1):
            for element in buckets[i]:
                result.append(element)
                if len(result) == k:
                    return result
            