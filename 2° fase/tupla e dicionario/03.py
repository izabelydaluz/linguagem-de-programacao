#03

tupla = [("julia", 23),("carlos", 20),("vini", 16)]
idade = []


for v in tupla:
    idade.append(v[1])

for v in tupla:
    if v[1] == max(idade):
        print(v)
        

