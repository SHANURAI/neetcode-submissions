class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        result = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                size = 1
                while num + size in hash_set:
                    size += 1 
                result = max(size, result)
        return result
        