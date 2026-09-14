class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x, y in points:
            heapq.heappush(heap, ((x**2 + y**2)**0.5, (x,y)))
        
        return [list(x[1]) for x in heapq.nsmallest(k, heap)]