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
    
class dpgnz_mysql():
    def __init__(self):
        self.host='10.11.13.63'
        self.user='root'
        self.password='Bb92293--'
        self.database='mysql'
        self.charset='utf8'
        self.db=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset)
        self.cursor=self.db.cursor()
    # 方法一  
    # def connect_mysql(self):
    #     db=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset)
    #     cursor=db.cursor()
    #     cursor.execute("SELECT VERSION()")
    #     data = cursor.fetchone()
    #     print(data)
    #     if data != None:
    #         print("数据库连接成功！")
    #     else:
    #         print("数据库连接失败！")

    # 方法二    
    # def connect_mysql(self,host,user,password):
    #     db = pymysql.connect(host=host,user=user,password=password)
    #     cursor=db.cursor()
    #     cursor.execute("SELECT VERSION()")
    #     data = cursor.fetchone()
    #     print(data)
    #     if data != None:
    #         print("数据库连接成功！")
    #     else:
    #         print("数据库连接失败！")
    
    # 重构方法一   
    def connect_mysql(self):
        try:
            db=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset)
            cursor=db.cursor()
            data1 = cursor.execute("SELECT VERSION()")
            data = cursor.fetchone()
            print("游标在：",data1)
            print(data)
            if data != None:
                print("数据库连接成功！")
            else:
                print("数据库连接失败！")
        except ConnectionError as e:
            print(e)  

    def push_sql(self,sql):
        print(pymysql.connect.cursor())
        try:
            cursor=pymysql.connect.cursor()
            cursor.execute(sql)
        except RuntimeError as e:
            print(e)
        pass
    
    def get():
        pass
    
    def close_mysql():
        pass
    
if __name__ == '__main__':
    db = dpgnz_mysql()
    # 方法一调用
    db.connect_mysql()
    # 方法二调用
    # db.connect_mysql("10.11.13.63","root","Bb92293--")
    