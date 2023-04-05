# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
            if len(stack) > 0 and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)