class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[ord(char) - ord('a')] += 1
            if tuple(chars) not in hash_table:
                hash_table[tuple(chars)] = []
            hash_table[tuple(chars)].append(s)
        return list(hash_table.values())



        