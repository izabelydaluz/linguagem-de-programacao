# 8.Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

n1 = float(input("informe a largura da parede"))
n2 = float(input("informe a altura da parede"))

area = n1*n2
litros = area /2

print(f"a area da parede é de:{area}, e a quantidade de litros é de:{litros}")