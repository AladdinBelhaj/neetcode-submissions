class Solution:
    def isPalindrome(self, s: str) -> bool:
        return ''.join([char for char in s if char.isalnum()]).lower()[::-1] ==''.join([char for char in s if char.isalnum()]).lower()
        