Algoritmo "tipos de pagamento - escolha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/03/2025
Var

nome, forma_de_P : caracter
quantidade : inteiro
preco , desconto , valor_total , total_da_compra : real


Inicio

escreva ("informe o nome do produto:")
leia (nome)

escreva ("informe a quantidade :")
leia (quantidade)

escreva("informe o preco:")
leia (preco)

 total_da_compra <- (quantidade * preco)

 escreval("valor total é de:" , total_da_compra)

escreval ("forma de pagamento dinheiro (1), cartao de credito (2), parcelado em 2 vezes(3), parcelado em 3 vezes(4)")
leia(forma_de_P)


escolha forma_de_P

       caso "1"
         desconto <- (total_da_compra * (10 /100))
           valor_total <- (total_da_compra - desconto)
                       escreval("o valor total a se pagar é", valor_total)
               
       caso "2"
         desconto <- (total_da_compra - (5/100))
          valor_total <- (total_da_compra - desconto)
                      escreval ("o valor a se pagar no cartão é de:", valor_total)
                      
       caso "3"
         valor_total <- (total_da_compra / 2)
                     escreval("valor total de cada parcela será de:", valor_total)
                     
                     
       caso "4"
          valor_total <-(total_da_compra / 3)
            valor_total <- valor_total + (5/100)
                        escreval ("valor total de cada parcela é de:" , valor_total)

       
       

fimescolha
Fimalgoritmo