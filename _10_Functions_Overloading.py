# def add2(a, b):          # --> add_int_int
#     return a+b

# def add3(a, b, c):       # --> add_int_int_int
#     return a+b+c


# def add(*args):
#     match len(args):
#         case 2:
#             return add2(*args)
#         case 3:
#             return add3(*args)


# #----------------------------------------------------
# print(add(1, 2))

# print(add(1, 2, 3))     # --> add_int_int_int
# print(add(1, 2))        # --> add_int_int

# function signature --> name, no. of args, types of args, sequence of the types


## Virtual Environments ###################################

# 1. Create a virtual env               py -m venv .venv-<name>
#    (with specific py version)             
# 2. Activate the environment           source .venv-trng/Scripts/activate  OR   .venv-trng/Scripts/activate.bat
#                                       pip list 
# 3. Install specific modules           pip install multipledispatch
# 3. Install requirement file           pip install -r requirements.txt
# 3. Create requirement file            pip freeze > requirements.txt
# 4. Work with proj
# 5. Deactivate the environment         deactivate

from multipledispatch import dispatch

@dispatch(int, int)
def add(a:int, b:int):
    print("2 ints")
    return a+b

@dispatch(int, int, int)
def add(a, b, c):
    print("3 ints")
    return a+b+c

@dispatch(float, float)
def add(a:float, b:float):
    print("2 float")
    return a+b

@dispatch(str, str)
def add(a:str, b:str):
    print("2 str")
    return a+b

print(add(1, 2))
print(add(1, 2, 3))
print(add(1.1, 2.2))
print(add("One", "One"))
