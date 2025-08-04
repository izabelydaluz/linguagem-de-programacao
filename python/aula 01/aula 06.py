#declaração de variaveis
a = 5
b = 7.8
c = "iza"
d = True

#vizualizando os tipos de variaveis
print (type(a))
print (type(b))
print (type(c))
print (type(d))

#mostrando para o usuario a variavel a.
print(a)

#mostrando string para o usuario - não esqueçam as aspas ''/""
print('hello word!! ^,^')

nome = "alberto"
valor = 9
print("o valor digtado foi:", valor)

#usando o print formatado(f) para juntar variaveis com textos
print(f"olá {nome}, o valor depositado foi de {valor} reais")

# ---------------------------INPUT-------------------------#

nome = input("informe seu nome:  ")
idade = input("informe sua idade:  ")


print(f"olá {nome}, tudo bem bem?!, voce tem {idade} anos")


#---------------EXEMPLOS---------------------#
# int = interio
# float = real

n1 = float(input("informe um numero: "))
n2 = float(input("informe outro valor: "))

soma = n1 + n2

print(f"a soma dos valores {n1} {n2} é {soma}")

# #---------------OPERADORES-------------------#

a = 7
b = 2

soma = a+b
mult = a*b

#a elevado b (7 elevado a 2)
pota = a**b

# b elevado a (2 elevado a 7)
prtb = b**a
div = a/b
divr = a//b
restdiv = a%b

# linha 63 e 66 são a mesma coisa
print(f"resultados:\n{soma}\n{mult}\n{pota}\n{prtb}\n{div}\n{divr}\n{restdiv}")

print(f"resultados: \n\
      soma={soma}\n\
      multiplicação:{mult}\n\
      potencia de a: {pota} \n\
      potencia de b: {prtb} \n\
      divisão: {div}\n\
      devisão resto zero: {divr}\n\
      resto da divisão: {restdiv}\n \ ")

