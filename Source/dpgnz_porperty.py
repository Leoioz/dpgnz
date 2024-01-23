'''
Author      : Leoioz
Date        : 2024-01-23 19: 27: 49
LastEditors: Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-23 19:52:06
FilePath: \dpgnz\Source\dpgnz_porperty.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''
'''
description: 
return {*}
'''
class dpgnz_porperty:
    def __init__(self) -> None:
        pass
    
    def logger(function):
        def wrapper(*args,**kwargs):
            print(f"{function.__name__}:start")
            out = function(*args,**kwargs)  
            print(f"{function.__name__}:end")
            return out
        return wrapper

@dpgnz_porperty.logger
def some_function(text):
    print(text)
    
if __name__ == '__main__':
    some_function("hello world")
    pass
    
    
