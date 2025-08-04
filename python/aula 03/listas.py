#-------------LISTAS----------------

#[] -> utilizar
#armazernar em uma variavel
#separa por ,

# () -> tupla- lista imutavel
# [] ->
# {} ->

task = ["estudar", "fazer comida"]
print (task[1]) #-> com exemplo de posição
tasks = [1 , 2 , 3, "capivara", True]
print(tasks) # -> sem o exemplo
print(tasks[-1]) # com exemplo de index negativo

#mostra por posição -> index(começa com 0)
#ex task[0]= estudar
#task [1]

# se usar index negativos ele começa de traz para frente 
#ex (print[-1])

#fatiamento de lista , acessar um conjunto de valores da lista
#conseguimos "fatiar" a lista usando :

tast = ["chocolate-quente", "monica", "chuva", "uva", "sol", "celular" , 7 ]
print(type(tast)) # usei para saber qual era o tipoda minha lista
tast[4] = "lua" # ->modificar elementos(lista mutavel)
print(tast)

print(tast[1:5])
print(tast[:3])
print(tast[5:])

#------------------adicionando valores a lista---------------------
tas = ["chocolate-quente", "cebolinha", "chuva", "uva", "sol", "iphone" , 7 ]
print(tas)

tas.append("chocolate-quente")
print(tas)

tas.insert(4, "capim")
print(tas)

tas.insert(3, "comer") # ->inset adiciona um index na lista na posição que eu escolher
print(tas)


#-----------------------função del ()---------------------------
#--serve para alterar(retirar) algo da lista

del (tas[1])
print(tas)
# se tiver 2 nomes iguais mas em posições diferentes ele tira do primeiro

ta = ["chocolate-quente", "cebolinha", "chuva", "uva", "sol", "iphone" , 7 ]
print(ta)
ta.remove("chocolate-quente")
print(ta)

itemremovido = ta.pop(0) #pop -> exclui um item da lista e cola em outro lugar(tipo ctrl c ctrl v)
print(ta)
print(itemremovido)

#-----------metodos úteis em listas---------------

#-sort() = ordena por ordem alfabetica
#o sort so funciona em frases do mesmo tipo|ex:só letra ou só numero

t = ["chocolate-quente", "cebolinha", "chuva", "uva", "sol", "iphone"  ] # somente letras
print(t)

t.sort() #
print(t)

t.sort(reverse=True) #-> inverte a vizualização da lista
print(t)

roberto = [1, 2, 5, 6,0, 11  ] #somente lnumeros
roberto.sort()
print(roberto)

#-len() -> retorna o tamanho da lista | len(t)
#--count(valor)-> conta quantas vezes o valor aparece |t.count("ler")
#---index(valor)-> retorna o indice do valor |t.index(valor)

sofia = [1, 2, 3, 4,5, 6  ] #terminar dps
print(sofia)


#---copy()-> faz uma copia da lista
#--clear() -> remove os itens da lista
#-concatenação(+) -> junta os valores de duas linhas |combinada = roberto + novo_roberto

tom = ["azul", "vermelho", "roxo", "amarelo","rosa", "verde"  ]
print(tom)

alan = ["arvore", "faca", "papibaquigrafo","camisa", "caneta", "funil", "julgular"]
print(alan)

tom.copy() # copia
print(tom)

tom.clear() # limpa a lista
print(tom)
#----------------------concatenação(+)-----------------------

marcos_castro = ["azul", "vermelho", "roxo", "amarelo","rosa", "verde"  ]
print(marcos_castro)

felipe_neto = ["arvore", "faca", "papibaquigrafo","camisa", "caneta", "funil", "julgular"]
print(felipe_neto)

combinada = marcos_castro + felipe_neto
print(combinada)

#---------------------FOR--------------------

#usado para percorrer uma lista

#variavel -> itens serão armazenados aq
#lista -> a estrutura que será percorrida

task =["dormir", "ler", "comer"] # vai ser repetida 3 vezes pois possui 3 palavras
for a in task :
 print(a)
 print(a)
 print(a)

for lista in task:
 print(f"itens da lista: {lista}")

valores = [1,9,12,34,16,28]
soma = 0

for i in valores:
 print(f"valor da lista: {i}")
 soma = soma + i # mesma coisa que: soma += i
 print(f"soma: {soma}")

alberto = ["dormir", "comer", "treinar", "escrever"]
for indice, i in enumerate(alberto): #enumerar a lista
  print(f"{indice}: {i} ")

#-----------condição de parada--------

feija0 = ["dormir", "comer", "treinar"]
for i in range(3): # repetição da lista e parada forçada
  print(i)

#adicione 3 itens a uma lista 
lista1 = []
for i in range(3):
 item = input("informe o item da lista: ")
 lista1.append(item)
 print(lista1) # se o print estiver fora do for a lista só será mostrada no final
 
lista2 = []
for i in range(3):
 item = input("informe o item da lista: ")
 lista2.insert(0,item) # ele inverte a lista
 print(lista2)

 #adicionar 5 valores 

valores= []
for i in range(5):
 valor = float(input("informe um valor: "))
 valores.append(valor)
 soma = soma + valor
print(f"soma: {soma}")

#jeito que o renzo ensinou
soma = 0
for i in range(5):
 var = float(input('informe um número: '))
 soma = soma + var
print (f'Soma de tudo: {soma}')

#sum = soma tds os elementos da lis
# len = qtd de itens dessa lista
