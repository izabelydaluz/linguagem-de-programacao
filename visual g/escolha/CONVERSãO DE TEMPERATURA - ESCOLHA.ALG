Algoritmo "conversão de temperatura - escolha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/03/2025
Var

k, c , Re , f : real
converter : caracter

Inicio

escreva("informe a temperatura em °c:")
leia (c)

escreva ("informe para qual temperatura deseja converter (k (1),f(2),Re(3):")
leia(converter)

escolha converter

      caso "1"
       k  <-  (C + 273.15)
          escreva("a temperatura em °k é de:", k)
          
      caso "2"
      f <- (C * 1.8) + 32
           escreva ("a temperatura em °f é de:" , f)
           
      caso "3"
       Re <-  (C * 0.8)
          escreva ("a temperatura em °Re é de:", Re)

      outrocaso
         escreva ("so aceitamos a coverção em k , f e Re ")

fimescolha
Fimalgoritmo