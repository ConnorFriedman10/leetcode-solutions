class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = []
        count = 0

        for pos, spd in sorted(zip(position, speed))[::-1]:
            laps = (target-pos)/spd
            if not fleets or fleets[-1] < laps: #otherwise <=
                count += 1
            elif fleets[-1] >= laps:
                laps = fleets[-1]
            fleets.append(laps)
        return count