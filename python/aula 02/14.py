# 14.Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: 
# •	Soma de 2 n´umeros. 
# •	Diferença entre 2 números (maior pelo menor). 
# •	Produto entre 2 números. 
# •	Divisão entre 2 números (o denominador não pode ser zero).

n1 = float(input("informe um valor: "))
n2 = float(input("informe outro valor: "))

pergunta = input ("qual a operação escolhida?\n"
"1-Soma de 2 numeros\n"
"2-Diferença entre 2 números (maior pelo menor)\n"
"3-Produto entre 2 números\n" \
"4-Divisão entre 2 números(o denominador não pode ser zero)\n"
"resposta: ")

if pergunta == "1" :
    soma = n1 + n2 
    print(f"seu resultado é de {soma}")

if pergunta == "2":
    diferenca = n2-n1
    print(f"a diferença entre os dois é de: {diferenca}")
    
if pergunta == "3":
    produto = n1*n2
    print(f"o produto entre eles é : {produto}") 

if pergunta == "4":
    divisao = n1/n2
    print(f"a divisão entre eles é : {divisao}") 

else:
    print("erro. opção invalida")