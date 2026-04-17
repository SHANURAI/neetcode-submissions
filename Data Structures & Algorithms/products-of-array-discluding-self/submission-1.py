class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        proizv = 1
        result = []
        count_of_0 = nums.count(0)
        if count_of_0 > 1:
            return [0 for i in range(len(nums))]
        else:
            for num in nums:
                if num != 0:
                    proizv *= num
            for num in nums:
                if num == 0:
                    result.append(proizv)
                elif count_of_0 == 1:
                    result.append(0)
                else:
                    result.append(int(proizv / num))
        return result
    
        