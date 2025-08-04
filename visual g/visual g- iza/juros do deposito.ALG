Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/03/2025
Var

  juros, deposito, vf, juros_em_real: real

Inicio

  escreva(" qual o valor do deposito")
  leia (deposito)
  
  escreva (" qual a porcentagem de juros desses investimentos? %")
  leia (juros)
  
  juros_em_real <- deposito*(juros/100)
  vf <- deposito + juros_em_real

  escreva("no fim do seu mes vc terá R$", vf)
  escreva("voce teve", juros_em_real, "em juros")

Fimalgoritmo