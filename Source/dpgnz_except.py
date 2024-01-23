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
    
    
