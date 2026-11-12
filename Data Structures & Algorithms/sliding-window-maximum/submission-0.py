class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # deque method --> 
        # a larger number appears, discard from front
        # out of bounds, discard back 

        deque_list = deque()
        res = []
        
        if nums == []:
            return []

        for i in range(len(nums)):
            
            # window check --> if not empty and biggest element not in window
            # remove the number
            if deque_list and deque_list[0] <= i - k:
                deque_list.popleft()

            # remove front if find a bigger element (need to loop through entire deque)
            while deque_list and nums[deque_list[-1]] < nums[i]:
                deque_list.pop()
            
            deque_list.append(i)

            if i + 1 >= k:
                res.append(nums[deque_list[0]])

        
        return res
            

            





