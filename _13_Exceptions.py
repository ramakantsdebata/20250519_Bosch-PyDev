from random import randint
def Baz():
    print("Baz")

def Bar():
    print("Bar")
    if randint(0,1):
        pass
    raise ZeroDivisionError("Problem occured!!")
    # raise IndexError("Problem occured!!")
    Baz()

def Foo():
    print("Foo")
    try:
        Bar()
    except ArithmeticError as ex:
        print(f"\tEXCEPTION(foo): {ex}")
        print(f"\tEXCEPTION(foo): {str(ex)}")
        print(f"\tEXCEPTION(foo): {repr(ex)}") # Object representation
        print(f"\tEXCEPTION(foo): {ex!r}") # shorthand for repr()
        print("\tSome cleanup work...")
        print("\t...")
        print("\tCouldn't handle the exception completely")
        print("\tRe-raising the same exception")
        raise

def Main():
    print("Main")

    try:
        print("Starting...")
        Foo()
        print("Ending...")
    except (OverflowError, ZeroDivisionError) as ex:
        print(f"\n\tEXCEPTION(main): {ex!r}")
        # print("\t Handled exception")
        print("\tRe-raising the exceptino yet again")
        raise
    except Exception as ex:
        print(f"\n\tEXCEPTION(main): {ex!r}")
        print("\t Handled exception")


    print("Normal code execution resumes")
    print("End of Main")

Main()
