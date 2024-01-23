'''
Author      : Leoioz
Date        : 2024-01-22 17: 57: 29
LastEditors : Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-23 10: 47: 25
FilePath    : \dpgnz\Source\dpgnz_except.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''

class MyCustomException(Exception):
    def __init__(self, message="This is a custom exception"):
        self.message = message
    
    def __str__(self):
        return f'MyCustomException: {self.message}'
        
# 测试自定义异常类
try:
    raise MyCustomException("Something went wrong")
except MyCustomException as e:
    print(e)
    
    
