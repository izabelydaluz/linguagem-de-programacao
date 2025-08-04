Algoritmo "genero e contribuição - se,senao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/03/2025
Var

   idade, contribuicao: inteiro
   genero : caracter


Inicio
   escreva("informe seu genero:")
   leia (genero)

   escreva("informe seus anos de contribuição dentro da empressa:")
   leia (contribuicao)

   escreva ("informe sua idade:")
   leia (idade)

   se ( genero = "homem") e (idade >= 65) e (contribuicao >= 30)entao
      escreva("vc pode se aposentar")
senao

    se (genero = "mulher") e (idade >= 60) e (contribuicao >= 25) entao
       escreva("voce pode se aposentar")
       
     senao
          escreva("voce não pode se aposentar")
    fimse
   fimse
Fimalgoritmo