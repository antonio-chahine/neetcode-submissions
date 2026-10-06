class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        result = 1
        nums.sort()

        streak = 1
        for i in range(len(nums)-1):

            if nums[i+1] == nums[i]:
                continue
            elif abs(nums[i+1] - nums[i]) == 1:
                streak += 1
            else:
                streak = 1

            result = max(result, streak)
        
        return result


        