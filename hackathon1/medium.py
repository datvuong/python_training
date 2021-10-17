import re

def anagram_number(number):
    if isinstance(number, int):
        origin_number = str(number)
        reverse_number = origin_number[::-1]
        if origin_number == reverse_number:
            result = True
        else:
            result = False
    else:
        result = False
    return result

def roman_to_int(s):
    mapping_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    s = s.upper()
    check_s = re.match(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', s)
    last_value = 0
    number_int = 0
    if check_s:
        for k in s:
            cur_value = mapping_dict[k]
            if cur_value <= last_value:
                number_int += last_value
            else:
                number_int -= last_value
            last_value = cur_value
        number_int += last_value
    return number_int
