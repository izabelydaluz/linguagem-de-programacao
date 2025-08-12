#06

while True:
    nome = input("informe seu nome: ")
    idade = int(input("informe sua idade: "))

    if idade <= 16:
        print(f"{nome}, voce não pode votar ainda")
    if idade >= 18 or idade < 65:
        print(f"{nome}, voce é obrigado a votar perante a lei")
    if idade == 16 or idade == 17 or idade > 65:
        print(f"{nome}, voce não é mais obrigado a votar perante a lei")