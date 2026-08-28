class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        hm = {
            "DOWN":n,
            "RIGHT":1,
            "LEFT":-1,
            "UP":-n
        }
        return sum(hm[command] for command in commands)