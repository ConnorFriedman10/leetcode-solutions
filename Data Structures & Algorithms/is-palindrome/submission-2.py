class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s.lower() if x.isalnum()])
        print(len(s)//2 + (2*(len(s)%2 == 1) or 1))
        print(len(s))
        print(s[:len(s)//2])
        print(s[len(s)//2 + (2*(len(s)%2 == 1) or 1):][::-1])
        if len(s) == 1 or len(s) == 0:
            return True
        if (s[:len(s)//2] != s[len(s)//2 + 1*(len(s)%2 == 1):][::-1]):
            return False
        return True
        