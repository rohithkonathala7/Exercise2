from a.baseshapes import Shapes


class Rectangle(Shapes):
    def __init__(self, l, b):
        super().__init__(l, b)

    def perimeter(self):
        print("Perimeter of Rectangle is:", 2 * (l + b))


class Square(Shapes):
    def __init__(self, l):
        super().__init__(l, l)

    def perimeter(self):
        print("Perimeter of Square is:", 4 * l)


class Triangle(Shapes):
    def __init__(self, l, b):
        super().__init__(l, b)

    def perimeter(self, d, c):
        print("Perimeter of Triangle is:", l + d + c)


a = input("Which shape do you want to find the area,perimeter(rectangle, square, triangle): ")
match a.lower():
    case "rectangle":
        l = int(input("Enter the length: "))
        b = int(input("Enter the breadth: "))
        r = Rectangle(l, b)
        r.recarea()
        r.perimeter()
    case "square":
        l = int(input("Enter the length: "))
        s = Square(l)
        s.sqarea()
        s.perimeter()
    case "triangle":
        d = int(input("Enter the 1st side: "))
        l = int(input("Enter the 2nd side: "))
        c = int(input("Enter the 3rd side: "))
        b = int(input("Enter the height: "))
        t = Triangle(l, b)
        t.trarea()
        t.perimeter(d, c)
    case default:
        print("No shape found")
