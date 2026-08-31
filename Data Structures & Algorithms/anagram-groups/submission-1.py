class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs_hashmap = {}
        
        for string in strs:
            letter_count_arr = [0] * 26

            for char in string:
                letter_count_arr[ord(char) - ord('a')] += 1 # 'a' == 80, to map to 0 -> -80

            letter_count_str = ','.join(str(c) for c in letter_count_arr)

            if letter_count_str not in strs_hashmap:
                strs_hashmap[letter_count_str] = [string]
            else:
                strs_hashmap[letter_count_str].append(string)

        return strs_hashmap.values()



        