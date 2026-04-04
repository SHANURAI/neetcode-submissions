class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            if len(indexes) > 0:
                if indexes.get(target - nums[i]) != None:
                    return [indexes[target - nums[i]], i]
            indexes[nums[i]] = i
        return [0, 0]