class Solution:
    def trap(self, height: List[int]) -> int:
        
        # ith block: min height of the two maximum on either side - 
        #   ith height

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        total = 0
        i = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                

            else:
                r -= 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]
        
        return total




            