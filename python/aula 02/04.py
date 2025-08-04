# 4.Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input("informe o seu nome:")
resposta = input("voce gosta do seu nome?")

if resposta == "sim":
    print(f"{nome}, realmente é um nome lindo ")
else:
    print("se ame!")
