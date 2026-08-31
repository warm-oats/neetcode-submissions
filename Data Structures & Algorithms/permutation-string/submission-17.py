class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq_map = defaultdict(int)

        for letter in s1:
            s1_freq_map[letter] += 1

        end_index = 0

        for start_index in range(len(s2)):
            s1_freq_map[s2[start_index]] = -1 + s1_freq_map.get(s2[start_index], 0)

            while s1_freq_map[s2[start_index]] < 0:
                s1_freq_map[s2[end_index]] += 1
                end_index += 1
            
            if (start_index - end_index + 1) == len(s1):
                return True
        
        return False
            


        


