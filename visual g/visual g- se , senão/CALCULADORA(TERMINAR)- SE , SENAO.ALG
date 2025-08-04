Algoritmo "calculadora(terminar)- se , senao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2025
Var
// Seção de Declarações das variáveis 
valor_01 , valor_02 , valor_final: real
operacao_mat : caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva ("escolha um valor:")
leia(valor_01)
escreva("escolha o segundo valor:")
leia(valor_02)
escreva("informe a operação matematica desejada:")
leia(operacao_mat)

se (operacao_mat = "adição") entao
   valor_final <- valor_01 + valor_02
  escreva("seu rultado é", valor_final)
senao
 se (operacao_mat = "subtração")  entao
    valor_final <- valor_01 - valor_02
    escreva("seu resultado é:", valor_final)
senao
  se (operacao_mat = "multiplicação") entao
     valor_final <- valor_01 * valor_02
      escreva("seu resultado é:", valor_final)
senao
   se (operacao_mat = "divisão") entao
     valor_final <- valor_01 / valor_02
      escreva ("seu resultado é", valor_final)
   fimse
  fimse
 fimse
fimse

Fimalgoritmo