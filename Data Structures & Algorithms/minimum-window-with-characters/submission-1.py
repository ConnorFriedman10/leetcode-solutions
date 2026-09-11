class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        missing = len(t)  # total characters still needed to satisfy the window
        left = 0
        best_left, best_right = 0, 0
        found = False

        for right, ch in enumerate(s):
            if need.get(ch, 0) > 0:
                missing -= 1
            need[ch] = need.get(ch, 0) - 1

            while missing == 0:
                if not found or (right - left) < (best_right - best_left):
                    best_left, best_right = left, right + 1
                    found = True

                left_ch = s[left]
                need[left_ch] = need.get(left_ch, 0) + 1
                if need[left_ch] > 0:
                    missing += 1
                left += 1

        return s[best_left:best_right] if found else ""