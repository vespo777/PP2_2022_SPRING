class Shape():
    def __init__(self, l):
        self.l = int(input())
    def area(self):
        print(self.l**2)
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self, l)
        
x=Square(Shape)
x.area()    

