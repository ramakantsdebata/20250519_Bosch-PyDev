
#region Define Earlier (Python) vs Define Higher (C/C++/Java/DotNET)

# def Bar():
#     """
#     Author: Ramakant
#     Bar Function
#     Called by Foo()
#     In turn calls Baz()
#     """
#     print("Bar")
#     Baz()

# def Foo():
#     print("Foo")
#     Bar()
#     Baz()

# def Baz():
#     print("Baz")

# def Main():
#     print("Main")
#     Foo()
#     print(Bar.__doc__)


# Main()

#endregion

#region Return statement
# def calc(a, b):
#     sum = a + b
#     prod = a * b
#     return sum, prod

# ret = calc(1, 2)

# print(ret, type(ret))

#endregion

#region Passing Args

## Positional parameters
def add(a, b):
    print(f"{a=}, {b=}")
    return a + b

print(add(1, 2))
print(add(2, 1))

## Named Parameters / KeyWorded Parametered
print(add(b=2, a=1))

#endregion
