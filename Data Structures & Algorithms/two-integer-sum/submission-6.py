class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# O(n)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
        return []

        l, r = 0, len(nums) - 1

        while l < r:
            curSum = nums[l] + nums[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []