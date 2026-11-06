class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest_length = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest_length = max(longest_length, r - l + 1)

        return longest_length

        