class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s.lower() if x.isalnum()])
        if (s != s[::-1]):
            return False
        return True
        