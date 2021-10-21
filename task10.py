def common_char(string1,string2):
    set1 = set(string1)
    set2 = set(string2)
    common_char = list(set1 & set2)
    common_char = ', '.join(common_char)
    print('Common letters:', common_char)