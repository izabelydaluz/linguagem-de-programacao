#03

nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))

if idade<= 2:
    print(f"{nome}, voce pertence ao berçario")
elif idade >= 3 and idade <=6:
    print(f"{nome}, voce pertence a educação infantil")
if idade >= 7 and idade <=10:
    print(f"{nome}, voce pertence ao fundamental nivel I ")
elif idade >= 11 and idade <=15:
    print(f"{nome}, voce pertence ao fundamental nivel II")
if idade >= 16 and idade >=18:
    print(f"{nome}, voce pertence ao ensino medio")