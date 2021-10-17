from datetime import datetime, timedelta
import re
# 1
def day_diff(release_date, code_complete_day):
    release_date = datetime.strptime(release_date, '%d/%m/%Y')
    code_complete_day = datetime.strptime(code_complete_day, '%Y-%d-%m')
    num_day = (release_date - code_complete_day).days
    return num_day

# 2
def alpha_num(sentence):
    all_list = re.findall(r'\w+', sentence)
    alpha_list = re.findall(r'[a-zA-Z]+', sentence)
    alpha_num_list = [x for x in all_list if x not in alpha_list]
    return alpha_num_list


