class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower() # strip only removes from end
        l, r = 0, len(s) - 1
        print(s)
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                return False
        return True