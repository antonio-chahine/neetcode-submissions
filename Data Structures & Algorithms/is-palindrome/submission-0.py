class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        compressed_str = ''
        for char in s:
            if char.isalnum() == True:
                compressed_str += char.lower()
            
        if compressed_str == compressed_str[::-1]:
            return True
        else:
            return False

        
        