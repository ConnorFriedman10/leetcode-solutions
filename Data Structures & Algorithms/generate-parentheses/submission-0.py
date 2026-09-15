class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #pretty simple, we can use a stack to track opposite pairings
        
        #keep track of left and right sides
        #add left until lcount == 0, and rent when lcount > rcount

        res = []
        
        def parenRecur(lcount, rcount, pst):
            if rcount >= n:
                res.append(pst)
                return
            
            if lcount < n:
                parenRecur(lcount+1, rcount, pst + "(")
            if rcount < lcount:
                parenRecur(lcount, rcount+1, pst + ")")
        
        parenRecur(0, 0, "")
        return res