# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        data = {'(': ')'}

        max_depth = 0

        for ch in s:
            if ch in data:
                stack.append(ch)
                if len(stack) > max_depth:
                    max_depth = len(stack)

            elif ch == data['(']:
                stack.pop()

        return max_depth
