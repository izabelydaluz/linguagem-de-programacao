Algoritmo "media de notas- se, senao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2025
Var
// Seção de Declarações das variáveis 
nome: caracter
media_final: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva ("informe seu nome:")
leia (nome)
escreva("informe sua media final:")
leia (media_final)

se (media_final < 5 ) entao
   escreva (nome, "aluno reprovado")
senao
 se (media_final >= 5  )e (media_final <= 6) entao
    escreva ( nome , "aluno em recuperacao")
senao
  se(media_final >= 7) entao
     escreva(nome , "aluno aprovado")
  fimse
 fimse
fimse
Fimalgoritmo