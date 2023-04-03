# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        scobes = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for ch in s:
            if ch in scobes:
                stack.append(ch)
            elif len(stack) == 0 or scobes[stack.pop()] != ch:
                return False

        if len(stack) != 0:
            return False

        return True