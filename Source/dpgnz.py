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

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def area(self):
#         return 3.14 * self.radius ** 2
#中文注释
#     @property
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# circle = Circle(5)
# print(circle.radius)    # 输出: 5
# print(circle.area)      # 输出: 78.5
# print(circle.perimeter) # 输出: 31.4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius
#中文注释

    @area.setter
    def area(self, value):
        self.radius = value ** 0.5
    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print(circle.radius)    # 输出: 5
print(circle.area)      # 输出: 78.5
print(circle.perimeter) # 输出: 31.4
