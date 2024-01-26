'''
Author      : Leoioz
Date        : 2024-01-24 11: 29: 57
LastEditors: Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-25 09:35:36
FilePath: \dpgnz\Source\dpgnz_log.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''
# 代码示例:
from dpgnz_core import *

logger.add("out.log", backtrace=True, diagnose=True)  # 注意，在生产环境中可能会泄露敏感数据


class dpgnz_log(Logger):
    def __init__(self) -> None:
        super().__init__()
        '''
        description: save_path，descr都是sink形参的子参
        return {*}
        '''
        self.save_path   = "./log/"    #用来放log文件路径
        self.descr       = "dpgnz_"        #用来加备注文字
        '''
        description: 往下是其他形参
        return {*}
        '''
        self.level       = ['TRACE',
                            'DEBUG',
                            'INFO',
                            'SUCCESS',
                            'WARNING',
                            'ERROR',
                            'CRITICAL'] #用来指定日志等级
        self.format_rule =  '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> ' \
                            '| <magenta>{process}</magenta>:<yellow>{thread}</yellow> ' \
                            '| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<yellow>{line}</yellow> - <level>{message}</level>'  
                                        #用来指定log信息格式
        self.filter_rule = filter_rule  #用于确定一条记录是否应该被记录到指定地点。
        self.colorize    = colorize     #用来指定log是否自动配色
        self.serialize   = serialize    #用来指定是否将日志装换为json格式
        self.rotation    = "10 MB"     #用来指定log文件多大，存放时间，是否循环存储等内容
        self.retention   = "30 days"    #用来放指定多少时间后进行清理
        self.compression = compression  #用来指定log文件是否压缩
        self.backtrace   = True    #用来跟踪异常，并把异常内容输出，这个会暴露源码
        self.diagnose    = True     #用来跟踪异常，并把变量内容和堆栈输出，这个会暴露源码
        self.enqueue     = enqueue      #用来将日志记录放入队列中，以避免多个进程记录到同一目的地时发生冲突。
        self.context     = context      #用来输出上下文对象或名称，enqueue为trues时，这个默认开启
        self.catch       = catch        #用来捕捉异常
        
        
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
    