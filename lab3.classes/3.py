class Shape():
    def __init__(self, l, w):
        self.l = int(input())
        self.w = int(input())
    def area(self):
        print(self.l * self.w)
class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self, l, w)

x=Rectangle(Shape, Shape)
x.area()

