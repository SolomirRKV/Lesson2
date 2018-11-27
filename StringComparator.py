def string_processer(str1 = '',str2 = ''):
    #if str1 is not str or str2 is not str:
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif len(str2) > len(str1) and str2 == 'learn':
        return 3



print(string_processer('a', 5))
print(string_processer('a', 'learn'))
print(string_processer('aa', 'b'))
print(string_processer('a', 'a'))
print(string_processer('a', 'learn'))
print(string_processer('learn', 'b'))
print(string_processer('learn', 'learn'))