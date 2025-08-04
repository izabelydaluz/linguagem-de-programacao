Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2025
Var

valor_da_compra: real
numero_de_parcelas:inteiro
valor_de_cada_parcela:real

Inicio

  escreva ("digite o valor da compra:")
  leia (valor_da_compra)
  
  escreva ("informe o numero de parcelas feitas")
  leia (numero_de_parcelas)
  
  valor_de_cada_parcela <- (valor_da_compra/numero_de_parcelas)
  
  escreval (" vc pagará", valor_de_cada_parcela, "reais em ", numero_de_parcelas, "parcelas")

Fimalgoritmo