class Player:
    def __init__(self,name):
        self.name = name

    def printname(self):
        print('Welcome', self.name)


p1 = Player('shrek')

p1.printname()

