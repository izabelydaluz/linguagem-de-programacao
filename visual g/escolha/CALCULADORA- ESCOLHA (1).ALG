Algoritmo "calculadora- escolha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/03/2025
Var
// Seção de Declarações das variáveis 

numero_01 , numero_02 , resultado_final: real
operacao: caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva ("informe o numero 01 : ")
leia (numero_01)

escreva ("informe o numero 02 : ")
leia (numero_02)

escreva("informe a operação desejada (+ - / *):")
leia (operacao)

escolha operacao :

       caso "+"
        resultado_final <-  (numero_01 + numero_02 )

     
       caso "-"
          resultado_final <- (numero_01 - numero_02)

     
       caso "/"
         resultado_final <- (numero_01 / numero_02)

          
       caso "*"
        resultado_final <- (numero_01  *  numero_02)



fimescolha
      escreval ("seu resultado é:" ,numero_01, operacao , numero_02 , "=" , resultado_final)

Fimalgoritmo