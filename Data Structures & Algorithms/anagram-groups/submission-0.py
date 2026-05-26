class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = { word : ''.join(sorted(word)) for word in strs}
        grouped = {}
        for word, sorted_ana in anagram_dict.items():
            grouped.setdefault(sorted_ana, []).append(word)

        return list(grouped.values())