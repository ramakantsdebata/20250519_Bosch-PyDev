# Tuple - Immutable ordered collection of non-homegeneous objects
tp1 = (1, 2, 3)
tp2 = tuple([1, 2, 3])
tp3 = tuple()

print(type(tp1), type(tp2), type(tp3))


tp4 = ()
print(type(tp4))

tp5 = (1,)
print(type(tp5))

tp6 = (1, 2, [3, 4, 5])
print(tp6)
print(tp6[0])
print(tp6[2])
tp6[2].append(6)
print(tp6)



lst = [tp1, tp2, tp3, tp4, tp5]
for x in lst:
    print("Checking ", x)
    hash(x)

dt = dict().fromkeys(lst)

print(dt)

## NAMED TUPLES ################################################

# idx(0): x; idx(1): y
p1 = (10, 20)
print("x: ", p1[0], "   y: ", p1[1])

from collections import namedtuple
# Point = namedtuple("Point", "x y")
Point = namedtuple("Point", ["x", "y"])
p2 = Point(10, 20)
print("x: ", p2[0], "   y: ", p2[1])
print("x: ", p2.x, "   y: ", p2.y)


Student = namedtuple("Student_ntup", "roll name std")
s1 = Student(1, "Pravin", 5)
s2 = Student(2, "Abhijeet", 16)

print(s1)
print(s2.roll, s2.name, s2.std)


lst = list(s1)
print(lst)

tp = (1, "Pravin", 5)
lst = list(tp)
print(lst)

dt = {"roll": 1, "name": "Pravin", "std": 5}
lst = list(dt)
print(lst)

print(type(s1))
