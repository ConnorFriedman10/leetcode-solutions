class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums = [-x for x in nums] #original list
        currwindow = nums[-k:] #current window
        heapq.heapify(currwindow)
        nnums = nums[:-k] #list to be popped
        removed = set() #add removed values 

        
        while nnums:
            while currwindow[0] in removed:
                removed.remove(heapq.heappop(currwindow))
            res.append(-currwindow[0])
            removed.add(nums.pop())
            heapq.heappush(currwindow, nnums.pop())
        
        while currwindow[0] in removed:
            removed.remove(heapq.heappop(currwindow))
        res.append(-currwindow[0])
        return res[::-1]