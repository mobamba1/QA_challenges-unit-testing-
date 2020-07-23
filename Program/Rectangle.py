class Rectangle:
    def __init__(self,height,width):
        self.vertices = 4
        self.sides = 4
        self.height = height
        self.width = width


    def area(self):
        return self.height * self.width

a = Rectangle(4,6)
print(a.area())

        