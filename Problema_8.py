a, b, c = input("Dati 3 cifre, separate prin spatiu (1xSpace) \t").split(" ")
comb1 = a + b + c   #Formam combinatiile de numere
comb2 = a + c + b
comb3 = b + a + c
comb4 = b + c + a
comb5 = c + b + a
print(comb1, comb2, comb3, comb4, comb5)