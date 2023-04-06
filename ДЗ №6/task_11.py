# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0

        while i < n:
            if len(stack) > 0 and stack[-1] == s[i].swapcase():
                stack.pop()
            else:
                stack.append(s[i])

            i += 1

        return ''.join(stack)