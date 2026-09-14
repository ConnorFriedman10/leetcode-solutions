class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if stone1 != stone2:
                heapq.heappush_max(stones, abs(stone1-stone2))
        
        if stones:
            return stones[0]
        return 0