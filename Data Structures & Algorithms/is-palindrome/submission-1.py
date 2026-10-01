class Solution:
    def isPalindrome(self, s: str) -> bool:
        checkPalindrome = ''.join([char for char in s if char.isalnum()]).lower()

        return checkPalindrome[::-1] == checkPalindrome