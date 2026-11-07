from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counts = Counter(s1)

        s1_len = len(s1)

        if s1_len > len(s2):
            return False

        l, r = 0, s1_len - 1

        window_counts = Counter(s2[l:r+1])

        while r < len(s2):

            if counts == window_counts:
                return True

            # Remove the character leaving the window
            window_counts[s2[l]] -= 1

            if window_counts[s2[l]] == 0:
                del window_counts[s2[l]]

            l += 1
            r += 1

            # Add the character entering the window
            if r < len(s2):
                window_counts[s2[r]] += 1

        return False