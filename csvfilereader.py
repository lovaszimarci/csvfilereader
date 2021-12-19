import csv




with open('1.csv', 'r') as file1:
    lista1 = csv.reader(file1)
    #ll = list(lista1)

with open('2.csv', 'r') as file2:
    lista2 = csv.reader(file2) 
    masodiklista = list(lista2)
    
elsolista = []

elsolista.append(lista1)

print(elsolista)


# osszeslista = elsolista + masodiklista

# print(osszeslista)
