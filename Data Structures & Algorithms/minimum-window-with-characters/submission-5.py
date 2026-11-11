class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or len(t) > len(s):
            return ""

        t_counts = Counter(t)

        l, r = 0, len(t) - 1

        shortest_substring = ""
        min_length = float('inf')

        window = s[l:r+1]
        s_counts = Counter(window)

        # NEW: Track satisfied character requirements
        need = len(t_counts)
        have = 0

        for c in t_counts:
            if s_counts[c] >= t_counts[c]:
                have += 1

        while r < len(s):

            # CHANGED: Instead of comparing Counters
            if have == need:

                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    shortest_substring = s[l:r+1]

                # Remove leftmost character
                s_counts[s[l]] -= 1

                # NEW: Check if a requirement is no longer satisfied
                if s[l] in t_counts and s_counts[s[l]] < t_counts[s[l]]:
                    have -= 1

                l += 1

            else:
                if r + 1 < len(s):
                    r += 1
                    s_counts[s[r]] += 1

                    # NEW: Check if a requirement has become satisfied
                    if s[r] in t_counts and s_counts[s[r]] == t_counts[s[r]]:
                        have += 1
                else:
                    return shortest_substring

        return shortest_substring