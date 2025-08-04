# Faça um programa que receba nome e a média de um aluno.
# a. Crie um dicionário para guardar a situação do aluno (aprovado, reprovado)
# b. No final mostre se o aluno foi aprovado ou reprovado

while True:
    nome = input("informe seu nome: ")
    media = float(input("informe sua media"))

    situacao = {"aprovado":"voce foi aprovado","reprovado":"voce foi reprovado"}
    if media >= 7:
        print(situacao["aprovado"])
    else:
        print(situacao["reprovado"])