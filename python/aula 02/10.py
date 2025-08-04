# 10.Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.

temp = input("olá, poderia me informar a tempertura atual?")

if temp > "20" :
    print(f"nossa {temp}, é muito quente")
elif temp == "20" : 
    print(f"{temp} é um bom clima")
else:
    print(f"uai {temp} é muito frio")
