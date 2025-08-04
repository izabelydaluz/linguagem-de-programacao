Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 09/03/2025
Var

nome , curso, diciplina : caracter
nota_01, nota_02, nota_03, media_final:real


Inicio

   escreva("digite seu nome:")
   leia(nome)
   escreva("digite seu curso:")
   leia(curso)
   escreva("informe sua diciplina")
   leia(diciplina)
   
   escreva("informe sua nota 01:")
   leia(nota_01)
   escreva("informe sua nota 02")
   leia(nota_02)
   escreva("informe sua nota 03")
   leia(nota_03)
   
   media_final <- (nota_01 + nota_02 + nota_03) / 3
   
   escreval("sua media em ", diciplina , "e de:", media_final)
Fimalgoritmo