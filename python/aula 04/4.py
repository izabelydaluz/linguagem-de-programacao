# 4) Escreva um programa que lido um número, calcule e informe o seu fatorial. Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

num = int(input("informe um numero: "))
i = num
while (i > 1):
    num *= (i - 1)
    i += - 1
print(num)
    
#mari:

numero = int(input("informe um numero: "))
antecessor = numero

while antecessor > 1:
    numero *= (antecessor - 1)
    antecessor -= 1

print (numero)

