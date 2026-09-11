class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[0],0)]
        final_idx = [0 for x in temperatures]

        for idx, temp in enumerate(temperatures[1:]):
            track_idx = 1
            while stack[-1][0] < temp and len(stack) > 0:
                pidx = stack.pop()[1]
                final_idx[pidx] = idx - pidx + 1
                track_idx += 1
                if not stack:
                    break
            stack.append((temp, idx+1))
        
        return final_idx
                    
            