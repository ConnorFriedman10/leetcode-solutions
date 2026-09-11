class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #1. n^2 loop that does a simple calculation and saves the values
        #2.
        maxWater = 0
        
        for left in range(len(heights)-1):
            for right in range(len(heights)-1, left, -1):
                if min(heights[left], heights[right]) * (right-left) > maxWater:
                    maxWater = min(heights[left], heights[right]) * (right-left)
        return maxWater
            
        