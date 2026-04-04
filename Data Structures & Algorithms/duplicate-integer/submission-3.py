class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_nums = set()
        for num in nums:
            if num in in_nums:
                return True
            in_nums.add(num)
        return False