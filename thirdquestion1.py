class Shapes:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def recarea(self):
        print("Area of Rectangle is:", self.l * self.b)

    def sqarea(self):
        print("Area of Square is:", self.l * self.l)

    def trarea(self):
        print("Area of Triangle is:", (self.l * self.b) / 2)
