class myclass:
    def getstring():
        pass
    def __init__(self, txt):
        self.txt=txt
    def printString(self):
        print(self.txt.upper())
p1=myclass(input())
p1.printString()