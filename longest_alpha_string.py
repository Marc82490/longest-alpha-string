def long_alpha_string(s):
    """
    Takes in a string of characters and finds the longest alphabetical substring.
    
    s: a string
    
    Returns: the longest alphabetical substring in s.
    """
    working_list = ""
    longest_substring = ""

    n = len(s)

    for k in range(n):
        for index in range(k+1):
            string_to_check = s[index : n-k+index]
            working_list = string_to_check[0]
            for i in range(len(string_to_check)):
                if i == 0:
                    continue
                if string_to_check[i] >= string_to_check[i-1]:
                    #if in alphabetical order
                    working_list += string_to_check[i]
                else:
                    #if not in alphabetical order
                    if len(working_list) > len(longest_substring):
                        longest_substring = working_list
                    working_list = string_to_check[i]
            if len(working_list) > len(longest_substring):
                #catches working_list once the iteration is complete
                    longest_substring = working_list
    
    return longest_substring
