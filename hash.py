import hashlib

# encoding GeeksforGeeks using md5 hash 
# function  
                       
str = "C:/xampp/htdocs/down"

md5str = hashlib.md5(str.encode())
dige = md5str.hexdigest()
print(dige)

"""
주소 : md5
파일명 : 원본
소유 그룹 : 박주호


소유 그룹
소유자 - 권한
"""