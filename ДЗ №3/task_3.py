# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.StupidPalindrome(s, l + 1, r) or self.StupidPalindrome(s, l, r - 1)

            l += 1
            r -= 1

        return True

    def StupidPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
