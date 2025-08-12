#04

nome = input("informe seu nome por gentileza: ")
idade = int(input("informe sua idade: "))
peso = float(input("informe seu peso: "))

if idade <= 15:
    print(f"{nome},voce nao pode doar sangue ainda")
elif idade == 16 and idade == 17 and peso >= 55:
    print(f"{nome},voce pode doar somente com autorização")
if idade >=18 and peso >= 60:
    print(f"{nome},voce pode doar ")
if idade > 69 :
    print(f"{nome},voce não pode mais doar")