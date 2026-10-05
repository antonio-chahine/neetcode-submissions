class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod, zero_count = 1, 0

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1

        res = []

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        
        if zero_count == 0:
            for i in range(len(nums)):
                res.append(prod//nums[i])
            return res
        

