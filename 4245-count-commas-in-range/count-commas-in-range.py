class Solution:
    def countCommas(self, n: int) -> int:
        str1 = str(n)
        length = len(str1)
        if length <=3:
            return 0
        return (n-999)