Algoritmo "estado civil da pessoa- se, senao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2025
Var
// Seção de Declarações das variáveis
nome , sigla: caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva ("informe seu nome")
leia (nome)
escreva ("informe sua sigla de estado civil (em maiusculo):")
leia(sigla)

se (sigla = "S" )entao
     escreva (nome , "voce é esta na pista")
senao
  se (sigla = "C") entao
     escreva (nome , "(in)felizmente voce é casado")
senao
   se (sigla = "V") entao
      escreva (nome , "meus pesames voce é viuvo")
senao
    se (sigla = "D") entao
       escreva (nome , "voce é divorciado, esta tudo bem?")
    fimse
   fimse
  fimse
 fimse
Fimalgoritmo