'''
Author      : Leoioz
Date        : 2024-01-22 17: 57: 29
LastEditors: Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-23 11:32:28
FilePath: \dpgnz\Source\dpgnz_except.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''
'''
description: 万能通用的异常类,你生成的实例，输入什么信息给他他就代表什么异常，无聊的print
return {*}
'''
class GeneralException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
    
    def __str__(self):
        return f'GeneralException: {self.message}'

# 自定义异常类的调用


    
