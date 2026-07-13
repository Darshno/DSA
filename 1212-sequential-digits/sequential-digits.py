class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []

        for start in range(1, 10):
            num = start

            for nxt in range(start + 1, 10):
                num = num * 10 + nxt

                if low <= num <= high:
                    res.append(num)

        return sorted(res)