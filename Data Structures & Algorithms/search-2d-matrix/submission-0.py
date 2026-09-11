class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = []
        for row in matrix:
            li += row
        
        l, r = 0, len(li)

        while l < r:
            m = l + ((r - l) // 2)
            if li[m] > target:
                r = m
            elif li[m] <= target:
                l = m+1
        return True if (l and li[l - 1] == target) else False
            