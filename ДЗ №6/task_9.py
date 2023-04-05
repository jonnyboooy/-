# https://leetcode.com/problems/remove-outermost-parentheses/description/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        current_depth = 0
        result = ''

        for ch in s:
            if ch == '(':
                current_depth += 1
            elif ch == ')':
                current_depth -= 1

            if (current_depth == 1 and ch != '(') or current_depth > 1:
                result += ch

        return result