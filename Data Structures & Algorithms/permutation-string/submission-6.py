class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        st1 = list(s1)
        st1.sort()
        st2 = list(s2)

        if s1 in s2:
            return True

        left = 0
        right = len(st1)

        while right <= len(s2):
            currset = st2[left:right]
            currset.sort()
            if currset == st1:
                return True
            left += 1
            right += 1
        return False
        