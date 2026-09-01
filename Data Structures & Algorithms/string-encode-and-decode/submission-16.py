class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for word in strs:
            encoded_str += str(len(word)) + "#" + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []

        if not s:
            return []

        i = 0

        while s:
            word_len = ''

            while s[i] != '#':
                word_len += s[i]
                i += 1

            s = s[i+1:]
            int_word_len = int(word_len)

            if int_word_len == 0:
                res.append("")
            else:
                res.append(s[0:int_word_len])
                s = s[int_word_len:]
            
            i = 0
        
        return res
                    








