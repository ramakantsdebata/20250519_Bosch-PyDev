import sys
import os

from _12_Cars import *

def demo_sys():
    print(sys.version)
    print(f"{sys.path = }")
    print(f"{sys.argv = }")
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = None

    if name:
        print(f"Hi {name} !")
    else:
        print("Hi there !!")

    print(f"{sys.base_exec_prefix = }")
    print(f"{sys.exec_prefix = }")

    if sys.base_exec_prefix == sys.exec_prefix:
        print("We are currently NOT in any virtual env.")
    else:
        print("We are executing from inside a virtual environment")

def demo_os():
    current_dir = os.getcwd()
    print(f"{current_dir = }")

    # Create a folder in the CWD
    new_dir =  os.path.join(current_dir, "demo_dir")
    print(f"{new_dir = }")

    if os.path.exists(new_dir):
        print(f"Folder [{new_dir}] already exists!")
    else:
        os.mkdir(new_dir)
        print(f"New dir created at: {new_dir}")
    
    # List the files and folders in the current folder
    print("\nFiles and folders in the current directory :")
    for item in os.listdir(current_dir):
        print(f"\t{item}")

    new_file = os.path.join(new_dir, "demo_file.txt")
    print(f"{new_file = }")

    # Option 1
    try:
        file = open(new_file, "w")
        file.write("This is a text data\n")
        file.write("Some more text\n")
        data = ["Data1\n", "Data2\n", "Data3\n"]
        file.writelines(data)
        file.flush()
        file.write("Last line\n")
        # file.close()
    except FileExistsError as ex:
        # file.close()
        print(f"EXCEPTION: {ex!r}")
        raise
    finally:
        file.close()

    # Option 2 - Context Manager block
    with open(new_file, "w") as file:
        file.write("This is a text data\n")
        file.write("Some more text\n")
        data = ["Data1\n", "Data2\n", "Data3\n"]
        file.writelines(data)
        file.flush()
        file.write("Last line\n")

    if os.path.exists(new_file):
        with open(new_file, "r") as file:
            s1 = file.read()
            print("\n", "-"*40)
            print(s1)
            print("\n", "-"*40)

        with open(new_file, "r") as file:
            data = file.readlines()
            print(type(data), data)

            print("'"*40)
            file.seek(0)
            print(f"{file.tell() = }")
            data = file.readlines()
            print(type(data), data)
            print(f"{file.tell() = }")


    # Remove the file
    if os.path.exists(new_file):
        os.remove(new_file)
    print(f"Removed the file [{new_file}]")

    # Remove the directory/folder
    if os.path.exists(new_dir):
        os.rmdir(new_dir)

def Main():
    # demo_sys()
    demo_os()


Main()

# Test3()
