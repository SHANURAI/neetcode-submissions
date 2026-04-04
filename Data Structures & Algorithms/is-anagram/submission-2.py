class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        for char in s:
            if char not in ss:
                ss[char] = 0
            ss[char] += 1
        for char in t:
            if char not in tt:
                tt[char] = 0
            tt[char] += 1
        return ss == tt
