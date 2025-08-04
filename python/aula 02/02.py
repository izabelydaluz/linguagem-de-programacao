# 2. Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

nome =  input("informe seu nome: ")
idade = float(input("informe sua idade: "))

if idade > 18 :
    print(f"{nome} voce é maior de idade")

elif idade == 18 :
    print(f"{nome} voce ja é maior de idade")

else:
    print(f"{nome} voce é menor de idade. vaza!")
 