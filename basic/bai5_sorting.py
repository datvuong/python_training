# Sorting - Sắp xếp điểm thi
# Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (m1, m2, e) gồm:
# m1 = midterm1
# m2 = midterm2
# e = endterm
# Cho một list gồm danh sách điểm thi của sinh viên 1 lớp. Viết chương trình Python để 
# sắp xếp danh sách trước theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple (sắp xếp theo điểm cuối kỳ - endterm tăng dần).
# vd sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) == [(10, 2, 1), (9, 1, 2), (3, 2, 3), (6, 4, 4), (1, 2, 5)]

marks = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]

sorted_marks = sorted(marks, key=lambda x: x[2])
print(sorted_marks)

# Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường
# Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). Viết hàm đảo ngược thứ tự các từ trong chuỗi và 
# đổi tất cả các chữ cái từ hoa thành thường và ngược lại. (kết quả là "Chicken The For Coming Is Fox The")
s = "tHE fOX iS cOMING fOR tHE cHICKEN"

import re
def reverse_string(string):
    string = re.split(r'\s', string)
    string = ' '.join(string[::-1])
    string = ''.join([c.upper() if c.islower() else c.lower() for c in string])
    return string

reverse_string(s)

# Regex - ApacheLog
# Logfile của webserver apache gồm nhiều dòng với mỗi dòng có định dạng như sau
# 10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET xxxxxx HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
# Trong đó xxxxxx có thể là đường dẫn đến một thư mục hoặc file bất kỳ của server.
# Dùng regex để lọc lấy ra tất cả các đường dẫn đến file .jpg trong các file log đầu vào dưới đây.
# Loại bỏ các đường dẫn trùng nhau và trả ra danh sách các đường dẫn.
# Định dạng của mỗi đường dẫn trả ra trong list nên là:
# "http://host/path" với
# host là phần cuối của tên logfile
# path là phần xxxxxx được trích xuất phía trên
# Input Logfiles
import re

image_link = []
for file in ['place_code.google.com', 'animal_code.google.com']:
    count = 0
    with open(f"ApacheLog/{file}", 'r') as f:
        while True:
            count += 1
            line = f.readline()
            if not line:
                break
            
            match_obj = re.search(r'"GET\s+(.*\.jpg)\s+HTTP/1.0"', line)
            if not match_obj:
                continue
            
            link = 'http://{file}{path}'.format(file=file, path=match_obj.group(1))
            image_link.append(link)

print(image_link[0:5])
