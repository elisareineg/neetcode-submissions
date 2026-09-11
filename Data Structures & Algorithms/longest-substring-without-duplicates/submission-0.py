class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength


