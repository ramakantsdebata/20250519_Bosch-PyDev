# Lambda (Anonymous functions):

double = lambda x: x*2
print(double(4))

Exp = []
Exp.append(lambda x: x**0)
Exp.append(lambda x: x**1)
Exp.append(lambda x: x**2)
Exp.append(lambda x: x**3)
Exp.append(lambda x: x**4)

a = 10

print(Exp[0](a))
print(Exp[1](a))
print(Exp[2](a))
print(Exp[3](a))
print(Exp[4](a))

print(Exp)


# Map Filter Reduce