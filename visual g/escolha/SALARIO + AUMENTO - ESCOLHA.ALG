Algoritmo "salario + aumento - escolha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/03/2025
Var

salario_final , faixa_salarial : real
aumento:real

Inicio

 escreva ("informe sua faixa sararial:")
 leia(faixa_salarial)
 
 escolha (faixa_salarial) :
 
 caso 1000 ate 1500
 
      aumento <- faixa_salarial * (10 / 100)
        salario_final <- aumento + faixa_salarial
      
       escreva ("seu salario final é", salario_final)
       
  caso 1501 ate 2000
  
        aumento <- faixa_salarial * (8 / 100)
         salario_final <- aumento + faixa_salarial

        
         escreva("seu salario final é", salario_final)
         
    caso ( >= 2000)
    
          aumento <- faixa_salarial * ( 5 / 100)
            salario_final <- aumento + faixa_salarial

          
           escreva ("seu salario final com aumento é de:", salario_final)
fimescolha


Fimalgoritmo