def add(a:int, b:int) -> int:
   res = a + b
   if a == 0:
        print("A is '0'")
   return res

print(add(1, 2))

print(add(1.5, 2.5))

print(add("Test", "Data"))
