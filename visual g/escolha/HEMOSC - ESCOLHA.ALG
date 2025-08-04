Algoritmo "HEMOSC - escolha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/03/2025
Var

nome , interessa  :caracter
idade :inteiro
peso : real

Inicio
escreva("infome seu nome :")
leia (nome)

escreva("infome sua idade :")
leia (idade)

escreva("infome seu peso :")
leia (peso)


se (idade <= 15 ) entao
       escreva (nome ," vc ainda não possue idade o suficiente")
       
  se(idade >= 16) e(peso >= 50) entao
           escreva (nome , "voce pode doar sangue")
           
   se (idade >= 18)  e ( peso >= 50) entao
      escreva (nome, "fique a vontade para doar sangue")

    se (idade >= 69) entao
       escreva(nome, "voce não pode mais ser um doador...")

      senao
        escreva (nome, "voce não pode doar pois seu peso é muito baixo")



    fimse
   fimse
  fimse
fimse

Fimalgoritmo