class Square:
    def __init__(self, a):
        self.a = a
    
    def perimeter(self):
        return 4*self.a
    
    def area(self):
        return self.a * self.a

class Rectangular:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b

objs = []
for a, b in [(2,3), (5,2), (8,10), (4,5), (8,2)]:
    objs.append(Square(a))
    objs.append(Rectangular(a, b))

def print_details(obj):
    print("Chu vi:", obj.perimeter())
    print("Dien tich:", obj.area())

for obj in objs:
    print_details(obj)