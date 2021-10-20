def common_char(string1,string2):
    set1 = set(string1)                 # converting first string to set
    set2 = set(string2)                 # converting a second string to a set
    common_char = tuple(set1 & set2)    # checking for characters in both sets
    return (common_char)