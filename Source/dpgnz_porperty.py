'''
Author      : Leoioz
Date        : 2024-01-23 19: 27: 49
LastEditors: Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-23 19:43:08
FilePath: \dpgnz\Source\dpgnz_porperty.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''
class dpgnz_porperty:
    def __init__(self) -> None:
        pass
    
    def logger(self,*args,**kwargs):
        def wrapper(*args,**kwargs):
            print(f"{function.__name__}:start")
            out = function(*args,**kwargs)  
            print(f"{function.__name__}:end")
            return out
        return wrapper
    
    
    
    
