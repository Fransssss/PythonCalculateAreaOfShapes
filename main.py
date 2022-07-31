# Author: Fransiskus Agapa

# =============================
class CommonValue:

    def __init__(self, side, base):
        self.side = side
        self.base = base


class Square(CommonValue):

    def __init__(self, side, base):
        super().__init__(side, base)   # check this - put one or two value base on parent class

    def area(self):
        return self.side * self.side


class Rectangle(CommonValue):

    def __init__(self, r_side, base):
        super().__init__(r_side, base)

    def area(self):
        return self.side * self.base


class Triangle(CommonValue):

    def __init__(self, side, base, height):
        super().__init__(side, base)
        self.height = height

    def area(self):
        return self.height * self.base
# =============================

print("\n== Calculate Area ==")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("E. Exit")
choice = input("choice: ").lower()  # make user input to lower case

ph = 0                              # placeholder - some functions wont need all values that are set in parent class

while choice != 'e':                # input will be made to lower case - no need to consider capital 'E'
    if choice == '1':
        print("\n[ Area of Square ]\n")
        try:
            print("Input side of the square: ", end=" ")           # end=" " -  prompt and user input in one line
            sq_side = int(input(""))
            square = Square(sq_side, ph)
            print("\n[ The area of the square: " + str(square.area()) + " ]")
        except ValueError:                   # possibility user do not input digit
            print("\n[ Value Error - Digit only ]")

    elif choice == '2':
        print("\n[ Area of Rectangle ]\n")
        try:
            print("Input side of rectangle: ", end=" ")
            r_side = int(input())
            print("Input base of rectangle: ", end=" ")
            r_base = int(input())
            rectangle = Rectangle(r_side, r_base)
            print("\n[ The area of the rectangle: " + str(rectangle.area()) + " ]")
        except ValueError:
            print("\n[ Value Error - Digit only ]")

    elif choice == '3':
        print("\n[ Area of Triangle ( given base and height ) ]\n")
        try:
            print("Input base of triangle: ", end=" ")
            t_base = int(input())
            print("Input height of triangle: ", end=" ")
            t_height = int(input())
            triangle = Triangle(ph, t_base, t_height)
            print("\n[ The area of triangle: " + str(triangle.area()) + " ]")
        except ValueError:
            print("\n[ Value Error - Digit only ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Calculate Area ==")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("E. Exit")
    choice = input("choice: ").lower()  # make user input to lower case

if choice == 'e':
    print("\n== Exit Program ==")