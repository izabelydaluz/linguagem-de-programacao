# 15.Leia a idade e o tempo de servico de um trabalhador e escreva se ele pode ou nao se aposentar. As condições para aposentadoria são: 
# 	• Ter pelo menos 65 anos, 
# 	• Ou ter trabalhado pelo menos 30 anos, 
# 	• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

g = input("informe seu genero[F ou M]:").upper
i = float(input("informe sua idade:"))
ts = float(input("informe seu tempo de serviço: "))

if g == "M" and i == 65 and ts == 30 :
    print("voce ja pode se aposentar")
else:
    print("voce não pode se aposentar ainda")

if g == "F" and i == 60 and ts == 25 :
    print("voce ja pode se aposentar")
else:
    print("voce não pode se aposentar ainda")

