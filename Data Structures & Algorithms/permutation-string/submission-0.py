class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counts = Counter(s1)

        s1_len = sum(counts.values())

        l, r = 0, s1_len - 1

        while r < len(s2):
            window = s2[l:r+1]
            window_counts = Counter(window)
            if counts == window_counts:
                return True
            else:
                l += 1
                r += 1
            
        return False
            
        
