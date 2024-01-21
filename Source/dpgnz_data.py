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

import pymysql
# db=pymysql.connect(host='10.11.13.63',user='root',password='Bb92293--',database='mysql',charset='utf8')
# cursor=db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print(data)
# if data != None:
#     print("数据库连接成功！")
# else:
#     print("数据库连接失败！")
    
class dpgnz_mysql(pymysql):
    def __init__(self):
        super().__init__()
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.charset=charset
        self.connect_mysql(host,user,password)
        
    def connect_mysql(self,host,user,password):
        self.db=pymysql.connect(host,user,password,database='mysql',charset='utf8')
        cursor=self.db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print(data)
        if data != None:
            print("数据库连接成功！")
        else:
            print("数据库连接失败！")
            
    def close_mysql():
        self.db.close()
        print("数据库连接已关闭！")
        
if __name__ == '__main__':
    db1 = dpgnz_mysql()
    db1.connect_mysql('10.11.13.63','root','Bb92293--')