class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result, carry = [], 0

        num1, num2 = num1.zfill(max(len(num1), len(num2))), num2.zfill(max(len(num1), len(num2)))

        for d1, d2 in zip(num1[::-1], num2[::-1]):
            carry, digit_sum = divmod(int(d1) + int(d2) + carry, 10)
            result.append(str(digit_sum))

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])


