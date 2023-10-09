import math 

print("\nAct1,a)")
x = float(input("Ingresa un valor decimal: "))
print(math.sqrt(x))

print("\nAct1,b)")
x = float(input("Ingresa un valor decimal: "))
print(abs(x))

print("\nAct1,c)")
x = float(input("Ingresa un valor decimal: "))
print(abs(x-3))

print("\nAct1,d)")
x = float(input("Ingresa un valor decimal: "))
print(math.sqrt(abs(x)))


print("\nAct3")
from funciones import repx3

cad = input("Dime algo: ")
print(repx3(cad))

print("\nAct4,a)")
def promX2(a,b):
    return (a+b)/2

print("\nAct4,b)")
x = float(input("numero real: "))
y = float(input("numero real: "))
print(promX2(x,y))

print("\nAct4,c)")

def promX3(a,b,c):
    return (a+b+c)/3

x = float(input("numero real: "))
y = float(input("numero real: "))
z = float(input("numero real: "))
print(promX3(x,y,z))

print("\nAct5")
def AbsVal(a):
    if a < 0:
        return a * -1
    else:
        return a

print("\nAct6,a)")
def exclamar(unaCadena):
    return "¡"+unaCadena+"!"
str = "1985"
print(exclamar(str))

print("\nAct6,b)")
def gritar(unaCdena):
    return "¡¡¡"+unaCdena+"!!!"
print(gritar("1985"))

print("\nAct7,a)")
print("# def elevarAlCubo(a):"+"\n"
     + "return a**3")
# def elevarAlCubo(a):
#     return a**3

print("\nAct7,c)")
from funciones import elevarAlCubo
print(0, "al cubo:", elevarAlCubo(0))
print(1, "al cubo:", elevarAlCubo(1))
print(2, "al cubo:", elevarAlCubo(2))
print(3, "al cubo:", elevarAlCubo(3))
print(4, "al cubo:", elevarAlCubo(4))
print(5, "al cubo:", elevarAlCubo(5))
print(6, "al cubo:", elevarAlCubo(6))
print(-1, "al cubo:", elevarAlCubo(-1))
print(-2, "al cubo:", elevarAlCubo(-2))
print(-3, "al cubo:", elevarAlCubo(-3))
print(-4, "al cubo:", elevarAlCubo(-4))
print(-5, "al cubo:", elevarAlCubo(-5))

print("\nAct8,a)")
def divisores(a):
    if a > 0:
        for i in range(1,a+1):
            if a % i == 0:
                print(f"{i} es divisor de {a}")
    else:
        for i in range(1,(a*-1)+1,):
            if a % i == 0:
                print(f"{i} es divisor de {a}")

print(divisores(-20))
