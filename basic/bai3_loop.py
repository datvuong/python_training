# For/While loop và Dictionary/Tuple/Set - Find Pair
# Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
# Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
# vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []
list_int = [3, 6, 7, 9, 11, 12]
sum_int = 18
result = []
len_list = len(list_int)
for i in range(len_list):
    a = list_int[i]
    for b in list_int[i+1:len_list]:
        ab = a + b
        if ab == sum_int:
            result.append((a, b))

# For/While loop và Dictionary/Tuple/Set - Unique value Dictionary
# Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.
# [VD1]: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.
# unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}
# [VD2]: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.
# unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}
list_dict = [dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
list_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_value = set()
for d in list_dict:
    unique_value = unique_value.union(d.values())

# For/While loop và Dictionary/Tuple/Set - Đếm ngược đến XMas
# Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
# vd in ra sau mỗi 5s:
# Countdown to Xmas 2021: 112 days, 11:47:01.339588
# Countdown to Xmas 2021: 112 days, 11:46:56.324008
# Countdown to Xmas 2021: 112 days, 11:46:51.310473
from datetime import datetime
import time
# xmas_date = datetime(2021, 12, 24, 23, 59, 59)
xmas_date = datetime(2021, 9, 7, 12, 32, 50)
countdown = True
while countdown:
    now = datetime.now()
    count = xmas_date - now
    days = count.days
    now_time = now.time()
    if count.total_seconds() <= 0:
        countdown = False
        break
    print(f'Countdown to Xmas 2021: {days} days, {now_time}')
    time.sleep(5)

# For/While loop và Dictionary/Tuple/Set - Đếm số
# Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
# my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
# Trả ra
# {10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
unique_number = set(my_list)
unique_dict = {}
for i in unique_number:
    number_count = my_list.count(i)
    unique_dict[i] = number_count
print(unique_dict)

# For/While loop và Dictionary/Tuple/Set - Print Star
# Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:
n = 10
for i in range(n):
    print((n-i+1)*'  ', (i+1)*'* ')

for i in range(2*n-1):
    if i < n - 1:
        star = (n-i+1)*'  ' + (i+1)*'* '
    elif i == n - 1:
        star = (n-i+1)*'  ' + (i+1)*'* ' + (2*n-i-1)*'* ' 
    else:
        star = (n+2)*'  ' + (2*n-i-1)*'* ' 
    print(star)

for i in range(2*n-1):
    if i == 0:
        star = '* ' + (i-1)*'  ' + (n-i+1)*'  '
    elif i < n - 1:
        star = '* ' + (i-1)*'  ' + '* ' + (n-i+1)*'  '
    elif i == n - 1:
        star = (i+1)*'* ' + (2*n-i-1)*'* ' 
    elif i > n - 1 and i < 2*n-2:
        star = (i+1)*'  ' + '* ' + (2*n-i-3)*'  ' + '* ' 
    else:
        star = (i+1)*'  ' + '* ' 
    print(star)
