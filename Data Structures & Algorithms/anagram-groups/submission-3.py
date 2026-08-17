class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        input: string list
        output: 같은 아나그램으로 list로 그룹화된 string들

        아나그램은 순서는 달라도 구성하고 있는 문자 종류와 개수가 같으면 됨
        """
        grouped = defaultdict(list)

        for word in strs:
            anagram_key = "".join(sorted(word))
            grouped[anagram_key].append(word)

        return list(grouped.values())