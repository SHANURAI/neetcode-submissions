class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []
        for element in nums:
            nums_hash[element] = 1 + nums_hash.get(element, 0)
        for key, value in nums_hash.items():
            buckets[value].append(key)
        for i in range(len(nums), 0, -1):
            if len(result) != k:
                result = result + buckets[i][:(k - len(result))]
            else:
                break
        return result
            