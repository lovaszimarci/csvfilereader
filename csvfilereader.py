import csv

with open('1.csv', 'r') as file1:
    lista1 = csv.reader(file1)
    for szam in lista1:
        li1  =  szam
    #ll = list(lista1)

with open('2.csv', 'r') as file2:
    lista2 = csv.reader(file2) 
    for szam in lista2:
        li2 = szam
    
osszeslista = li1 + li2
osszeslista = list(osszeslista)

for char in osszeslista:
    if osszeslista.count(char) > 1:
        osszeslista.remove(char)
        osszeslista.remove(char)
        
osszeslista = str(osszeslista)


with open('3.csv', 'w') as file3:
    file3.write(osszeslista)


