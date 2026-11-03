class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplet = []
        nums.sort()

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == 0:
                    triplet.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                elif three_sum > 0:
                    r -= 1

                elif three_sum < 0:
                    l += 1

        return triplet