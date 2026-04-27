class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(1, len(nums) - 1):
            j = 0
            k = len(nums) - 1
            target = -nums[i]
            while j < i and i < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return [list(x) for x in res]
