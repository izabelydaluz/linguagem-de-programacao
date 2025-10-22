# Elabore um script em linguagem Python com uma função que recebe como entrada um
# número ano e retorna True caso ano seja bissexto. Caso contrário, retorne Fals

def ano():
    a = int(input("informe um ano: "))
    if a%4 == 0:
        return "true"
    else:
        return "false"
    
print(ano())