class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        longest_length = 0
        char_dict = defaultdict(int)
        

        for r in range(len(s)):
            char_dict[s[r]] += 1
            
            most_frequent = max(char_dict.values())

            window_length = r - l + 1

            if (window_length - most_frequent) <= k :
                #valid
                longest_length = max(longest_length, window_length)
            else:
                char_dict[s[l]] -= 1
                l += 1
            
        return longest_length


            
            

        