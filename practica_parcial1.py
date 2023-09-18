print("\nAct2")




descuentan_el_dia = (input("Descuentan el dia? (si/no): "))
if descuentan_el_dia == "si" or "Si" or "SI":
    descuentan_el_dia = True
elif descuentan_el_dia == "no" or "No" or "NO":
    descuentan_el_dia = False

if descuentan_el_dia == True:
    paro_colectivos = input("Hay paro de colectivos? (si/no): ")
    if paro_colectivos == True:
        piquetes = bool(input("Hay piquetes? (si/no): "))
        if piquetes == True:
            print("Me veo obligado a adherirme")
    else: print("No me adhiero, voy a trabajar")
else: print("No me adhiero, voy a trabajar")

print("\nAct3")

chair1 = input("ingresa tu cadena: ")
chair2 = input("ingresa tu cadena: ")

newchair = ""

contador = 1
for i in chair1:
    if contador % 2 != 0:
        newchair = newchair + i
    contador = contador + 1

contador = 1
for i in chair2:
    if  contador % 2 == 0:
        newchair = newchair + i
    contador = contador + 1

print(newchair)

print("\nAct4")

terminos = int(input("Cuantos terminos deseas sumar?: "))

i = 1
total = 0
x = 2
y = 3
while i <= terminos:
    total = total + (x**i)/y
    print(x,"**",i,"/",y,"=",total)
    i = i + 1
    x = x + 1
    y = y + 1


