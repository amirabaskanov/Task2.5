a = int(input("Number of students in the first class: "))
b = int(input("Number of students in the second class: "))
c = int(input("Number of students in the third class: "))

class1 = a/2
if a%2 > 0:
    class1 = a/2 + 0.5
class2 = b/2
if b%2 > 0:
    class2 = b/2 + 0.5
class3 = c/2
if c%2 > 0:
    class3 = c/2 + 0.5
desks = class1 + class2 + class3
print(desks)
