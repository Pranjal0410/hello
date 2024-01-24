class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set()
        for l in s:
            if l not in a:
                a.add(l)
            else:
                a.remove(l)
        return len(s) - len(a) + 1 if len(a) else len(s)