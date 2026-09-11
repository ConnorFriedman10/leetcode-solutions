class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        left = 0
        right = 0
        charcount = {}

        while right < len(s):
            if s[right] not in charcount:
                charcount[s[right]] = 0
            charcount[s[right]] += 1

            if (right - left + 1) - max(charcount.values()) > k:
                charcount[s[left]] -= 1
                left += 1
            
            right += 1
        
        return right - left

        