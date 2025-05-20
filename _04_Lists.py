# List - Mutable Non homogeneous collection of objects

l1  = []
l2 = list()
print(type(l1), type(l2))
l2.append('A')
l2.append('B')

l3 = [1, 2, 3, 4, "Bangalore", "Pune", 12.3654]
l3.append(123)
print(l3)
print(str(l3))
print(l3.__str__())

l4 = list(l3)
print(l4)

l4.extend(l2)
print(l4)

l4.extend([1, 2, 2, 2, 3, 4, 7])
print(len(l4), l4.count(2))
print(7 in l4)


print("=$#"*80)
print(l2*5)
l5 = l2*5
print(l5)
l6 = [23, 98, 46, 95, 12]
print(min(l6))
print(max(l6))
print(sorted(l6))
print(sorted(l6, reverse=True))
print(l6)
print(l2 + l6)


l7 = list(['id', 'name', 'place'])
data = [l7]
data.append([1, "Ramesh", "Blore"])
data.append([2, "Vinayak", "Mumbai"])

print(data)
print(data[2])
print(data[2][1])

for idx in range(1, len(data)):
    print(data[idx][0])


str1 = "Manish"
str2 = str1
print(str1, str2)
print(id(str1), id(str2), sep="\n")
str2 += "!"
print()
print(id(str1), id(str2), sep="\n")
print(str1, str2)

def Modify(obj):
    obj.append(5)
    print(obj)


l1 = [1, 2, 3]
l2 = l1
print(id(l1), id(l2), sep="\n")
print(l1, l2)
l2.append(4)
print()
print(id(l1), id(l2), sep="\n")
print(l1, l2)
Modify(l1[:])

print(l1, l2)
