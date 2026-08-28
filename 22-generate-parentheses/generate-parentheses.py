class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def bt(oc,cc,curr):
            if oc == n and cc == n:
                result.append(curr)
                return
            if oc < n:
                bt(oc+1,cc,curr+"(")
            if cc < oc:
                bt(oc,cc+1,curr+")")
            if n == 0:
                return []
        bt(0,0,"")
        return result  