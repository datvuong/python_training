# get the max number from a list of numbers
print('Input 3 integer numbers:')
print('number a:')
a = int(input())
print('number b:')
b = int(input())
print('number c:')
c = int(input())
max_number = None
if a >= b:
    if a >= c:
        max_number = a
    else:
        max_number = c
else:
    if b >= c:
        max_number = b
    else:
        max_number = c
print(f'The max number is {max_number}')

# Check a year is a leap year or not.
print('Input a year to check:')
year = int(input())
if (year % 400 == 0) or ((year % 4==0) and (year % 100 !=0)):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is NOT a leap year.")

# BMI calculation
print('Chiều cao của bạn (m):')
h = float(input())
if h > 2.5:
    print("Chiều cao đã nhập không phù hợp. Nhập chiều cao đơn vị m. \nChiều cao của bạn (m)?:")
    h = float(input())
print('Cân nặng của bạn (kg):')
w = float(input())
bmi = w / (h * h)
if bmi < 17:
    print("Gầy độ II")
elif bmi < 18.5:
    print("Gầy độ I")
elif bmi < 25:
    print("Bình thường")
elif bmi < 30:
    print("Thừa cân")
elif bmi < 35:
    print("Béo phì độ I")
else:
    print("Béo phì độ II")
