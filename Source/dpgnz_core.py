'''
Author      : Leoioz
Date        : 2024-01-21 11: 08: 25
LastEditors: Leoioz 73148445+Leoioz@users.noreply.github.com
LastEditTime: 2024-01-23 17:52:40
FilePath: \dpgnz\Source\dpgnz_core.py
Copyright (c) 2024 by ${73148445+Leoioz@users.noreply.github.com}, All Rights Reserved. 
'''

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

from dpgnz_data import *
from dpgnz_except import *
from dpgnz_ui import *


class mywgeit(Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
        
if  __name__ == "__main__" :
    app = QApplication()
    window = QMainWindow()
    ui =Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    app.exec_()