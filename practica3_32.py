contador=1
for i in z:
    if contador <=3:
        legajo += i
    contador += 1
legajo+= "_"

contador = 1

for i in y:
    if contador <=3:
        legajo += i
    contador += 1

contador = 1

for i in x:
    if contador == 1 or contador == len(x) :
        legajo += i
    contador += 1 
print(legajo)
