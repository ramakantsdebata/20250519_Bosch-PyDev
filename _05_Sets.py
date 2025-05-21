# SET - Unordered Non-homogeneous Mutable collection of keys (immutables, whose state will be used for generating the hash-value)

x = "12345"
h = hash(x)
print(h)

l1 = [1, 2, 3, 4, 5]
# h2 = hash(l1)     <-- Only IMMUTABLES can be hashed
# print(h2)


s1 = set()
s1.add(1)
s1.add('A')
print(s1)
s2 = set(l1)
print(s2)
l2 = [1, 2, 3, [4, 5]]

for x in l2:
    print(x)
# s3 = set(l2)  < Error: iterable has a mutable element namely, the fourth one [4, 5]
s3 = set(s2)
print(s3)

s4 = {'b', 'c', 'a', 'g', 'd'}
print(s4)

s5 = set()
s5.add('b')
s5.add('c')
s5.add('a')
s5.add('g')
s5.add('d')
print(s5)

print(3 in l1)
print('b' in s5)

s5.add('a')
print(s5)
s5.update(l1)
print(s5)

s6 = {'c', 'd', 'e', 'f'}
s5.update(s6)
print(s5)

print("\n", "-"*40)
print(f"{s4=}")
print(f"{s6=}")
print(f"{s4.intersection(s6)=}")
print(f"{s4 & s6=}")
print(f"{s4.union(s6)=}")
print(f"{s4 | s6=}")
print(f"{s6 - s4 =}")
print(f"{s6 ^ s4 =}")

print("\n", "-"*40)
s7 = {'a', 'b', 'c'}
print(f"{s4=}")
print(f"{s7=}")
print(f"{s4.issubset(s7) = }")
print(f"{s4 <= s7 =}")
print(f"{s4.issuperset(s7) = }")
print(f"{s4 >= s7 =}")

print("\n", "-"*40)
print(f"{s6 = }")
s6.remove('c')
print(f"{s6 = }")
# s6.remove('c')


s6.discard('z')
print(f"{s6 = }")

print(f"{s6.pop() = }")

tmp = frozenset({'a', 'b'})
s8 = {tmp, 1, 2}
print(s8)

for elem in s8:
    print(elem, end= ' - ')
    # it = iter(elem)
    # for val in elem:
    #     print("\t", val)

print()
