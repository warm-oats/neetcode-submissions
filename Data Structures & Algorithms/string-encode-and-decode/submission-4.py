class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for word in strs:
            word_len = len(word)

            encoded_str += str(word_len) + '%' + word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        start_index = 0
        end_index = 0
        final_arr = []

        while start_index < len(s):
            if s[end_index] == '%':
                current_word_len = int(s[start_index:end_index])
                current_word = s[end_index+1:end_index+1+current_word_len]
                final_arr.append(current_word)

                start_index = end_index + 1 + current_word_len
                end_index = start_index
            else:
                end_index += 1
        
        return final_arr




