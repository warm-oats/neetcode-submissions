class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq_map = defaultdict(int)

        for letter in s1:
            s1_freq_map[letter] += 1

        s1_freq_map_copy = dict(s1_freq_map)

        for index, letter in enumerate(s2):
            s1_freq_map_copy = dict(s1_freq_map)
            end_index = index

            while end_index < len(s2) and s2[end_index] in s1_freq_map_copy:
                s1_freq_map_copy[s2[end_index]] -= 1

                if max(s1_freq_map_copy.values()) == 0 and min(s1_freq_map_copy.values()) == 0:
                    return True
                
                if min(s1_freq_map_copy.values()) < 0:
                    s1_freq_map_copy = dict(s1_freq_map)

                end_index += 1
        
        return False


        


