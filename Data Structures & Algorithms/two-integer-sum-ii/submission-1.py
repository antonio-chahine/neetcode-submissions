class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        res = []
        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                res.append(l+1)
                res.append(r+1)
                return res
            if two_sum > target:
                r -= 1
            if two_sum < target:
                l += 1

