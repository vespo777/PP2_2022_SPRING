import math
class pclass():
    def __init__(self):
        self.x = int(input())
        self.y = int(input())
    def show(self):
        print(self.x, self.y)
    def move(self):
        x1=int(input())
        y1=int(input())
        self.x=self.x+x1
        self.y=self.y+y1 
        print(self.x, self.y)
    def distan(self):
        print(math.sqrt(self.x**2+self.y**2))

p1=pclass()
p1.show()