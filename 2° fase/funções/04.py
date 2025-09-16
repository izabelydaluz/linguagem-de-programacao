#  Elabore um script em linguagem Python com uma função que recebe como entrada um
# número inteiro positivo e retorne a soma de todos os inteiros positivos menores ou iguais a
# n.
def soma():
    num = int(input("informe um numero: "))
    result = 0
    for v in range(num):
        result += (num - v)
        return v,result
    
v,result = soma()
print("a soma de {num} com seus antecessores é igual á {result} ")

    


