# Dictionary - Mutable, Non-homogeneous, Unordered collection of Key-Value pairs

dt1 = {1: "Bangalore", 2: "Mumbai", 3: "Delhi"}
print(type(dt1), dt1)

for key in dt1:
    print(key)

for key in dt1.keys():
    print(key)

for value in dt1.values():
    print(value)

for key, value in dt1.items():
    print(key, "-->", value)

dt2 = {}
print(type(dt2), len(dt2))

dt3 = dict()
print(type(dt3), len(dt3))

# dt4 = dict(1= "Bangalore", 2= "Pune")             # <-- ERROR: Tried to follow the pattern {k: v, k:v}, while the ctor accepts an iterable
dt4 = dict([[1, "Bangalore"], [2, "Pune"]])
print(">>>>", f"{dt4 = }")

l1 = [1, 2, 3]
dt5 = dict.fromkeys(l1)
print(dt5)

dt6 = dict({1: "Bangalore", 2: "Mumbai", 3: "Delhi"})
dt7 = dict(dt1)

l2 = list(dt1)
print(l2)


print(f"{dt1[2] = }")
# print(f"{dt1[5] = }")

print(f"{dt1.get(2) = }")
print(f"{dt1.get(5) = }")

dt1[5] = "Pune"

if 2 in dt1:
    dt1[2] = "Kolkata"      # <-- Update existing pair
if 5 not in dt1:
    dt1[5] = "Kolkata"      # <-- Add new pair

print(f"{dt1 = }")

dt1.update({5: "Chennai", 6: "Jaipur", 7: "Tezpur"})   # <-- Update existing; Add new
print(f"{dt1 = }")

print(len(dt1))

print(f"{dt1.popitem() = }")
print(f"{dt1.pop(5) = }")

print(f"{dt1 = }")

# l3 = [1, 2, 3, 4, 5]
# it1 = iter(l3)
# print(type(it1), it1)

# print(it1)
# while True:
#     print(next(it1))

for idx in dt1:
    print(idx, dt1[idx])

it2 = iter(dt1)
while True:
    idx = next(it2)
    print(idx, dt1[idx])
