Algoritmo "cursos- se ,senao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/03/2025
Var
// Seção de Declarações das variáveis 
nome, sigla, ADM , DIR , CEX : caracter


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("informe seu nome:")
leia(nome)
escreva ("informe a sigla do seu curso:")
leia(sigla)

se (sigla = "ADM") entao
   escreva ("bem vindo", nome , " ao curso de adiministração")
senao
 se (sigla = "DIR") entao
    escreva("bem vindo", nome , "ao curso de direito")
senao
  se (sigla = "CEX" ) entao
     escreva ("bem vindo", nome , "ao curso de comercio exterior")
  fimse
 fimse
fimse
Fimalgoritmo