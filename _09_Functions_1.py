
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

#region Passing Args  - Positional and Keyworded

# ## Positional parameters
# def add(a, b):
#     print(f"{a=}, {b=}")
#     return a + b

# print(add(1, 2))
# print(add(2, 1))

# ## Named Parameters / KeyWorded Parametered
# print(add(b=2, a=1))

#endregion

#region Packing/Unpacking and Variable parameters

# l1 = [1, 2, 3]
# print(l1)

# # a = l1[0]
# # b = l1[1]
# # c = l1[2]

# a, b, c = l1
# print(f"{a=}, {b=}, {c=}")

# def add(a, b, c=0):     # default argument   # L-value
#     return a+b+c

# l2 = [1, 2]

# print(add(l2[0], l2[1]))
# print(add(*l2))                     # R-Value; Use the '*' here to Unpackage
# print(">>", add(1, 2, 3))  # 6  
# print(">>", add(1, 2))     # 3

# # # Revision 1
# # def PrintNumber(a, b, c):
# #     print(f"{a=}")
# #     print(f"{b=}")
# #     print(f"{c=}")


# # # Revision 2
# # def PrintNumber(a, b, c=None):
# #     print(f"{a=}")
# #     print(f"{b=}")
# #     if c is not None:
# #         print(f"{c=}")

# # # Revision 3
# # def PrintNumber(lst):
# #     for val in lst:
# #         print(val)

# # Revision 4
# def PrintNumber(*coll):  # L-value side; Use the '*' here to Package
#     print(type(coll))
#     for val in coll:
#         print(val)

# PrintNumber(1, 2, 3)        # R-value
# PrintNumber(1, 2)
# PrintNumber(1, 2, 3, 4)

# # coll2 = []
# a, *b = 1, 2, 3
# print(type(a), a)
# print(type(b), b)

# print("\n", "-"*40)
# l3 = [1, 2, 3, 4, 5]
# # a, b, *c = l3
# # a, *b, c = l3
# *_, b, c = l3
# # print(type(a), a)
# print(type(b), b)
# print(type(c), c)

# l4 = [1, 2, 3]
# a, _, b = l4
# print(type(a), a)
# print(type(b), b)


# def add(a, b, *others):
#     for val in others:
#         print("\t", val)
#     print("End of val list")
#     sum  = a + b
#     for val in others:
#         sum += val
#     return sum

# # print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3, 4, 5))

# print("\n", "="*40)

# def PrintEmp(**emp):                        # Keyworded variable parameter
#     for key, val in emp.items():
#         print(key, "-->", val)

# PrintEmp(ceo="Rakesh", cto="Manish", cfo="Pravin")




# print("\n", "="*40)

# # Special Arguments
# # / --> enforces that args to LEFT of it can only be positional; args to RIGHT may be either postional or keyworded
# # * --> enforces that args to RIGHT of it can only be keyworded; args to LEFT may be either postional or keyworded


# def PrintNum(a, b, /, c, d, *, e, f):
#     pass

# PrintNum(1, 2, 3, 4, e=5, f=6)
# PrintNum(1, 2, c=3, f=4, d=5, e=6)      # Pos  / KwArg / VarArg / VarKwArg
# PrintNum(1, 2, 3, d=4, e=5, f=6)


# def PrintNum(a, b, c, d, e, f, /):       # ONLY positional args
#     pass

# def PrintNum(*, a, b, c, d, e, f):       # ONLY keyworded args
#     pass

#endregion

#region Scope

# LEGB

def print(*args):
    # Log the data (args) to files
    __builtins__.print(*args)

# from builtins import print

# print = __builtins__.print

def Outer():
    # global s1
    print(f"{locals()=}")
    s1 = "Outer string"
    print(f"{locals()=}")
    def Inner():
        # nonlocal s1
        s1 = "Inner string"
        print("Inner scope -->", s1)
    print(f"{locals()=}")
    Inner()
    print("Outer scope -->", s1)
    print(f"{globals()=}")
    globals()['s1'] = "Global Modified"
    # s1 = "Global Modified"

s1 = "Global string"

Outer()
print("Global scope -->", s1)

#endregion

