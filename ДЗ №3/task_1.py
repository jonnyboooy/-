# https://leetcode.com/problems/valid-palindrome/
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[,.:@#_;!\"\'\[\]\{\}\-\?\(\)\` ]', '', s).lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

