class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        
        left = 0
        currdict = {}
        max_length = 0
        idx = 0

        while idx < len(s):
            if s[idx] in currdict and currdict[s[idx]] >= left:
                left = currdict[s[idx]] + 1
            currdict[s[idx]] = idx
            max_length = max(max_length, idx - left + 1)
            idx += 1

        return max_length