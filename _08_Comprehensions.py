fruits = ["apple", "banana", "cherry", "dragonfruit", "elaichi", "fig", "guava", "kiwi"]

bowl = []
for fr in fruits:
    if 'a' not in fr:
        bowl.append(fr)

print(bowl)

l1  = [fr               for fr in fruits    if 'a' not in fr]
t1  = tuple(fr               for fr in fruits    if 'a' not in fr)
st1 = {fr               for fr in fruits    if 'a' not in fr}
dt1 = {fr:len(fr)       for fr in fruits    if 'a' not in fr}


print(type(l1), l1)
print(type(t1), t1)
print(type(st1), st1)
print(type(dt1), dt1)

## Public members for a type

obj = 10
public_members = [member         for member in dir(obj)       if not member.startswith("_")]
print(public_members)

## Public methods
public_methods = [member         for member in dir(obj)       if not member.startswith("_")]
print(public_methods)
