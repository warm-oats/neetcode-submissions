class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        
        for s in strs:
            encoded_str += '#' + str(len(s)) + '!' + s
        
        return encoded_str


    def decode(self, s: str) -> List[str]:

        start_index = 0
        end_index = 0

        res = []

        while (start_index < len(s)):
            if (s[end_index] == '!'):
                word_length = int(s[start_index+1:end_index])
                res.append(s[end_index+1:end_index+1+word_length])

                start_index = end_index + 1 + word_length
                end_index = start_index
            else:
                end_index += 1

        return res



