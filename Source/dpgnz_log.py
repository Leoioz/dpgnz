'''
Author      : Leoioz
Date        : 2024-01-24 11: 29: 57
LastEditors: Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-24 15:42:05
FilePath: \dpgnz\Source\dpgnz_log.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''
# 代码示例:
from dpgnz_core import *

logger.add("out.log", backtrace=True, diagnose=True)  # 注意，在生产环境中可能会泄露敏感数据


class dpgnz_log(Logger):
    def __init__(self) -> None:
        super().__init__()
        self.save_path=save_path    #用来放
        self.descr=descr#用来加备注文字
        self.rotation=rotation#用来放
        self.rotation=rotation#用来放
        self.rotation=rotation#用来放
        self.rotation=rotation#用来放
        
    def info_log_format(self):
        pass
    
    def error_log_format(self):
        pass
    
    def bug_log_format(self):
        pass
    
    def debug_log_format(self):
        pass
    
    def warning_log_format(self):
        pass
    
    def trace_log_format(self):
        pass
    
    def critical_log_format(self):
        pass
    
    def exception_log_format(self):
        pass
    