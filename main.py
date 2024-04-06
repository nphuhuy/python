import re

str = 'Hoc lap trinh Toidicode.com'
match = re.search(r'(.*) Toidicode.com', str)
if match: #nếu tồn tại chuỗi khớp                     
    print (match.groups()) # in ra chuỗi đó
else:
    print ('Khong tim thay!') # Không thì hiện thông báo
#Kết quả:
#('Hoc lap trinh',)