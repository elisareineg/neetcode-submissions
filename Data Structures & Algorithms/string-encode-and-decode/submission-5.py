class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        res = [] # build: read number until #, add next _ characters to res
        if not s:
            return res
        if s == "":
            return res
        i = 0
        while i < len(s): # j will start moving fwd, until next # and append the word up until s[i:j]
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end # move i to start of next length 

        return res

        