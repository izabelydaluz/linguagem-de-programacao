# 1Escreva um Programa que leia uma lista de 5 números inteiros e mostre-os

lista = [1,2,3,4,5,6]
print(lista)

# 2 Escreva um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

lista2 = []
for i in range(10):
 item = input("informe os numeros da lista: ")
 lista2.insert(0,item) 
 print(lista2)

#3 Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles.

valores= []
soma = 0
for i in range(5):
 valor = float(input("informe um valor: "))
 valores.append(valor)
 soma = soma + valor
print(f"soma: {soma}")

# #4 Escreve um Programa que leia uma lista com 5 itens, contendo itens repetidos e mostre os itens repetidos

#--count(valor)-> conta quantas vezes o valor aparece |t.count("ler")
#---index(valor)-> retorna o indice do valor |t.index(valor)

itens = []
repet = []

for i in range (5):
    item = input("informe os itens da lista: ")
    itens.append(item)
print(itens)

# if "maça" not in itens :
#   print("não está na lista")

for a in itens:
    if itens.count(a) > 1 and a not in repet:
        repet.append(a)

print(repet)

# 5-Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

numeros = []
par = []
impar = []

for i in range(5):
    num = int(input(f"informe um numero {i+1}°: "))
    numeros.append(num)
    
    if num  % 2 == 0 :
        par.append(num)
    else:
        impar.append(num)

print(f"lista completa numeros: {numeros}")
print(f"lista completa numeros: {par}")
print(f"lista completa numeros: {impar}")

# 6 Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.


medias = []

for qtdalu in range(3):
    nome = input("informe seu nome: ")
    soma = 0
    for  i in range(4):
        nota = float(input(f" {nome} informe sua nota {i+1}° : "))
        soma += nota         # soma = soma + nota
    mediaAluno = soma/4
    medias.append(mediaAluno)
print(medias)

qtdAprovados = 0
for i  in medias:
   if i >= 7 :
       qtdAprovados += 1
print(f"a quantidade de aprovados foi : {qtdAprovados}")

#7- Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos

idades = []
alturas = []

for a in range(3):
    idade = int(input("informe sua idade: "))
    altura = float(input("informe a sua altura: "))
    idades.append(idade)
    alturas.append(altura)

medAltura = sum(altura)/ len(altura)
print(idade)
print(altura)
print(medAltura)

qtdAlunos = 0

for a in range(len(idades)):
   if idades[a] > 13 and  alturas[a] < medAltura:
     qtdAlunos += 1

print(f"a quantidade de alunos com maiores de 13 anos com a altura menor que a média das alturas é de {qtdAlunos} alunos")


# Faça 4 listas:
# A. Filmes
# B. Jogos
# C. Livros
# D. Esporte
# a. Adicione no mínimo 2 itens em cada lista.
# b. Crie uma lista das 4 listas criadas acima.
# c. Acesse (mostrar) algum item da lista livros.
# d. Remova um item da lista esporte.

filmes = []
jogos = []
livros = []
esportes = []

for a in range(2):
  filme = input("informe um filme: ")
  filmes.append(filme)
  
  jogo = input("informe um jogo: ")
  jogos.append(jogo)

  livro = input("informe um livro: ")
  livros.append(livro)

  esporte = input("informe um esporte: ")
  esportes.append(esporte)

  #b 
  lista_comp = filmes + jogos + livros + esportes
  print(lista_comp)

  #c
print(livros[0])
  #d

del esportes[0]
print(esportes)