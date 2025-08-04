# --------- ESTRUTURAS DE REPETIÇÃO -----------------

i = 0 #inicializar o contador
while (i <= 10) : 
    print(i)
    i += 1 # incremento contador
print ("fim do programa")

# usar o brak para parar o codigo

while True:
    string_digitada = input("informe uma palavra: ")
    if string_digitada.lower() == "sair": #lower deixa em minusculo
        print("fim!")
        break

print("****operação de divisão**********")

while True:
    n1 = int(input("informe o 1° numero:  "))
    n2 = int(input("informe o 2° numero:  "))
    if n2 == 0:
        print("divisor = 0.\nencerrando o programa...")
        break
    print(f"{n1}/{n2} = {(n1/n2):.2f}")
print("-------------programa encerrado ---------")
    

# --------------contune----------------------------

num = 0
while num < 10 :
    num += 1
    if num %2 == 0:
        continue # ele irá ignorar os numeros pares
    print(num)
print(num)

print("EXEMPLO 3")

nomes = []
while True:
    nome = input("informe seu nome(ou fim para parar): ")
    if nome.lower() == "fim":
        break
    nomes.append(nome)
print("os nomes cadastrados foram: ")    
for v in nomes:
    print(v)
