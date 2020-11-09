import csv

datos=[["Nombre","edad"],["Emiliano","Juan"],[19,18]]

abrir=open('ejemplo2.csv','w')

with abrir:
    escritor=csv.writer(abrir)
    for x in datos:
        escritor.writerow(x)

print("Grabado con exito")

