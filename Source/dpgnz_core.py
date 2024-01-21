'''
MIT License

Copyright (c) 2024 Leoioz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import sys
import time
sys.path.append('..\\dpgnz\\ui')
from dpgnz_data import *
from dpgnz_ui import *

class mywgeit(Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        
if  __name__ == "__main__" :
    
    app = QApplication()#这句是为了新建一个窗口app
    
    window = QMainWindow()#这句是为了初始化咱们在pyside6里面的窗口，就是对象检查器的那个类
    
    ui =Ui_MainWindow()#这句是用我们自动生成的UI的类，生成一个实例
    # ui =mywgeit()
    
    ui.setupUi(window)#setupUi是UIform的函数，负责设置窗口的UI布局和组件，材料是QWidget类的实例
    #单步调试下来发现，其实widget是根本的窗口类，我们创建一个实例，有窗口得告诉窗口里面什么东西放哪里，而放的内容描述清单就是designer里面uic转出的py文件，setupui这个函数作用是把uifrom里面描述的布局内容，放置到qwidget的窗口中。
    window.show()
    app.exec_()
    
# 111
    # 32656654654