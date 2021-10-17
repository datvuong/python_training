def convert_tempature(c, convert_to):
    if not(isinstance(c, (int, float))):
        raise TypeError("param 'c' must be a number.")
    if convert_to == 'F':
        converted_t = c * 9/5 + 32
    if convert_to == 'K':
        converted_t = c + 273.15
    if convert_to == 'R':
        converted_t = (c + 273.15) * 9/5
    return converted_t


convert_tempature(100, 'K')

def convert_lenghth(lenghth, convert_to):
    if not(isinstance(lenghth, (int, float))):
        raise TypeError("param 'lenghth' must be a number.")
    if convert_to == 'm':
        converted_len = lenghth * 1000
    if convert_to == 'dm':
        converted_len = lenghth * 10000
    if convert_to == 'cm':
        converted_len = lenghth * 100000
    if convert_to == 'mm':
        converted_len = lenghth * 1000000
    if convert_to == 'mile':
        converted_len = lenghth * 1.609344
    if convert_to == 'inch':
        converted_len = lenghth * 39370.1
    return converted_len

convert_lenghth('100', 'mile')

def convert_second(sec):
    if not(isinstance(sec, (int, float))):
        raise TypeError("param 'sec' must be a number.")
    sec = int(sec)
    hour = sec//3600
    delta_hour = sec%3600
    min = delta_hour//60
    sec = delta_hour%60
    print(f"{hour} hours, {min} minutes, {sec} seconds")
    return (hour, min, sec)

convert_second(1000)

