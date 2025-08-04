Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2025
Var

 preco, juros, valor_final, valor_juros: real

Inicio

  escreva ("digite o preco do produto:")
  leia (preco)
  
  escreva("digite o acrescimo em juros:")
  leia (juros)
  
  valor_juros <- preco * juros/100
  
valor_final <- preco + valor_juros

escreval ("o valor final do produto sera de:", valor_final,"reais")
  

Fimalgoritmo