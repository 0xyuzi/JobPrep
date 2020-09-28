class Solution:
    def decodeString(self, s: str) -> str:
        # dfs method
        
        result = self.dfs(s,1)
        
        return result
    
    def dfs(self, encode_str, repeated_num):
        # check if sub_encode_str inside
        # pattern str(Int)+ "[" + sub_encode_str + "]"
        print(encode_str)
        suffix_str, sub_encode_str, k, prefix_str = self.is_sub_encode(encode_str)
        # print(suffix_str, sub_encode_str, k, prefix_str )
        if sub_encode_str:
            completed_decode_str = self.dfs(sub_encode_str, k)
            return k * (suffix_str + completed_decode_str + prefix_str)
        
        # if no sub_decode_str 
        else:
            return k * encode_str
            
    """
    find the first  "[" and if exist find the string of integer on the left side
    then suffix_str is the all string on the left hand side of the string integer 
    find the last "]" and all string on the right hand side is prefix_str 
    """    

    def is_sub_encode(self, encode_str):
        print(f"is_sub_encode function: encode_str {encode_str} ")
        suffix_str, repeated_k, index_right_bracket = self.search_repeated_num(encode_str)
        print(f"is_sub_encode function: :search_repeated_num returns: {suffix_str, repeated_k, index_right_bracket} ")
        if not suffix_str:
            return None 
        
        # if have suffix_str
        prefix_str, sub_encode_str = self.search_prefix_str(index_right_bracket, encode_str)
        
        return suffix_str, sub_encode_str, repeated_k, prefix_str
    
    # find the suffix_string and the repeated_k 
    def search_repeated_num(self, encode_str):
        for index, char in enumerate(encode_str):
            if char == '[':
                last_digit_index = index - 1
                first_digit_index = last_digit_index
                while( encode_str[first_digit_index] not in ['[', ']'] and 0<=int(encode_str[first_digit_index]) and int(encode_str[first_digit_index])<=9):
                    first_digit_index -= 1
        
        # if find the right bracket
        if index == len(encode_str) - 1:
            return None, None, None
        # if find the rightbracket
        first_digit_index = first_digit_index +1 
        suffix_str = encode_str[:first_digit_index]
        repeated_k = int(encode_str[first_digit_index:last_digit_indx+1])
        
        index_right_bracket = last_digit_indx+1
        
        return suffix_str, repeated_k, index_right_bracket
    
    # find the location of the right most bracket and return the sub_encode_str inside the leftmost bracket and rightmost bracket
    # return prefix_str, sub_encode_str
    def search_prefix_str(self,index_right_bracket, encode_str):
        
        left_most_bracket_index = 0
        
        for i in range(index_right_bracket, len(encode_str)-1):
            if encode_str[i] == ']':
                left_most_bracket_index = i
        
        return encode_str[: index_right_bracket], encode_str[index_right_bracket: left_most_bracket_index+1]