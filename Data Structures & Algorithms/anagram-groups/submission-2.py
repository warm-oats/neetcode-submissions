class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_group_hash = defaultdict(list)

        for word in strs:
            alphabet_dict = [0 for arr in range(28)]
            for letter in word:
                alphabet_dict[ord(letter) - ord('a')] += 1

            ana_group_hash[tuple(alphabet_dict)].append(word)

        return list(ana_group_hash.values())



