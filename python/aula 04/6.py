# 6) Elabore um programa que leia um número inteiro e indique se o número é primo
# ou não. Lembrando que os números primos são divisíveis somente por 1 e por ele
# mesmo. No entanto, o número 1 não é primo.

num = int(input("informe o valor: "))
divisao = 0

for v in range(1, num + 1 ):
    if num  % v == 0:
        divisao += 1
print(divisao)
if divisao == 2:
    print(f"seu valor {num} é primo")
else:
    print(f"seu valor {num} não é primo")
    

