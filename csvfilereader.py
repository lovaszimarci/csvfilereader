import csv

#opens the first csv file and add it to a variable as a list 
with open('1.csv', 'r') as file1:
    lista1 = csv.reader(file1)
    for szam in lista1:
        li1  =  szam
# opens the second csv file and add it to a variable as a list 
with open('2.csv', 'r') as file2:
    lista2 = csv.reader(file2) 
    for szam in lista2:
        li2 = szam
#sums up the two list from the csv files and add it to a variable as a list 
osszeslista = li1 + li2
# convert the summed list to a list (it is necessary for the for loop for some reason)
osszeslista = list(osszeslista)
#loops trough the summed list and cheks for duplicates 
for char in osszeslista:
    if osszeslista.count(char) > 1:
        # remove the duplicates twice --> it gives you only the ones that new and not used twice
        osszeslista.remove(char)
        osszeslista.remove(char)
# convert it to string --> only can write string format not list         
osszeslista = str(osszeslista)

# add the list to a csv file
with open('3.csv', 'w') as file3:
    file3.write(osszeslista)


# the with open form of opening files automatically close the files so there is no data leakage!!