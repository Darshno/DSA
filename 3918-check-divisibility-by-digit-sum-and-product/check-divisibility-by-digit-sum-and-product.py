class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        saa = [int(x) for x in s]
        sumx = 0
        prod = 1
        for x in saa:
            sumx += x
            prod *= x
        tot = sumx+prod
        if n%tot == 0:
            return True
        else:
            return False 