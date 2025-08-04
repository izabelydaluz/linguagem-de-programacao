#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto:
# a.	calcule a média anual das temperaturas;
# b.	mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temp = []

for v in range(12):
    temperaturas = float(input(f"digite a temperatura media do mês {v + 1}°: "))
    temp.append(temperaturas)
#a
media = sum (temp) / len(temp)
print(f"a media anual das temperaturas é de: {media: .2f}°")

#b
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

for v in range(12):
    if temp[v] > media :
        print(f"{meses[v]}: temp{temp[v]} °c : ")
  