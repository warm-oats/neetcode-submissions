class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_hash = defaultdict(list)

        for word in strs:
            ana_hash = [0] * 26

            for letter in word:
                ana_hash[ord(letter) - ord('a')] += 1

            result_hash[tuple(ana_hash)].append(word)

        return list(result_hash.values())