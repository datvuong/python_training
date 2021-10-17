# Function - Chỉ số thống kê mô tả
# Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:
# giá trị trung bình (mean) của dãy.
# trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. 
# Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
# mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".
# Lưu ý: kết quả trả ra sẽ là 1 list vì mode có thể nhiều hơn 1 giá trị.
# Vd:
# A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] ==> (mean(A), median(A), mode(A)) == (6.55, 7.0, [9])
# B=[4,4,5,4,5,5] thì (mean(B), median(B), mode(B)) == (4.5, 4.5, [4,5])
A = [0, 1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 10]

def mean(list_number):
    '''
    params
    list_number : A list of number to calculate the average.
    '''
    m = sum(list_number)/len(list_number)
    return m

mean(A)

def median(list_number):
    data = sorted(list_number)
    len_data = len(data) 
    mid_idx = len_data//2
    mod_idx = len_data%2
    if mod_idx == 0:
        m = (data[mid_idx-1] + data[mid_idx])/2 
    else:
        m = data[mid_idx]
    return m

median(A)

def mode(list_number):
    unique_number = set(list_number)
    unique_dict = {}
    for i in unique_number:
        number_count = list_number.count(i)
        unique_dict[i] = number_count
    max_val = max(unique_dict.values())
    m = [k for k,v in unique_dict.items() if v == max_val]
    return m

mode(A)

# Function - Đếm loại ký tự
# Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:
# s = "Hello World! 123"
# Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. 
# Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".
# a) Viết hàm trên dùng bất kỳ hàm built in nào của python
# b) Viết hàm chỉ dùng 1 hàm built in duy nhất.
# Gợi ý: Bộ ký tự đơn giản in ra màn hình được còn được gọi là bộ mã ASCII (đọc là 'As key') nguyên gốc gồm 128 ký tự. Bạn có thể in ra thử với câu lệnh sau.
# ASCII = "".join(chr(x) for x in range(33, 128))
# print(ASCII)
# Tài liệu tham khảo tiếng Anh. Bạn có thể tìm các tài liệu tiếng Việt các khái niệm tương tự có rất nhiều.
ASCII = "".join(chr(x) for x in range(33, 128))

s = "Hello World! 123"
def count_char_type(string):
    digits = '0123456789'
    char_lower = 'abcdefghijklmnopqrstuvwxyz'
    char_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_upper = sum([i in char_upper for i in s])
    num_lower = sum([i in char_lower for i in s])
    num_digits = sum([i in digits for i in s])
    char_type_dict = {
        'LETTERS': num_upper+num_lower,
        'CASE': {
            'UPPER CASE': num_upper,
            'LOWER CASE': num_lower
        },
        'DIGITS': num_digits
        }
    return char_type_dict

count_char_type(s)
