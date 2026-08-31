class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = defaultdict(list)

        for word in strs:
            alpha = [0] * 26
            ascii_offset = ord('a')

            for letter in word:
                ascii_num = ord(letter)
                ascii_i = ascii_num - ascii_offset

                alpha[ascii_i] += 1

            anag_map[tuple(alpha)].append(word)

        return list(anag_map.values())

        