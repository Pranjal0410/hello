class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = ord("A")
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            res = chr(columnNumber % 26 + a) + res
            columnNumber //= 26

        return res