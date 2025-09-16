#07

while True:
    nome = input("informe seu nome: ")
    peso = float(input("informe seu peso: "))
    altura = float(input("informe sua altura: "))

    imc = peso/(altura*altura)

    if imc < 18.5:
        print(f"{nome}, voce está abaixo do peso, seu imc é de: {imc}")
    if imc > 18.5 and imc < 25:
        print(f"{nome}, voce está no peso normal, seu imc é de: {imc}")
    if imc > 25 and imc <30:
        print(f"{nome}, voce está acima do peso, seu imc é de: {imc}")
    if imc > 30:
        print(f"{nome}, voce está obeso, seu imc é de: {imc}")