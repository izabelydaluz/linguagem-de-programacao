# faça uma tabuada de um numero informado pelo usuario

num = int(input("informe o numero da tabuada desejada: "))
i = 0 
n2 = num*10

while (i <= n2):
    print(i)
    i += num # incremento contador
    
# mari:
num = int(input("informe o numero da tabuada desejada: "))
cont = 0
while cont < 10 :
    cont += 1
    tabuada = num * cont
    print(f"{num} x {cont} = {tabuada}")