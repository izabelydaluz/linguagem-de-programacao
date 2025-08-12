#08

cont1 = 0
cont2 = 0
cont3 = 0


pessoas = int(input("informe quantos votantes são:"))

for i in range(pessoas):
    print("candidatos eleito\n1-deodoro\n2-floriano\n3-iza")
    op = int(input("informe o numero do candidato votado: "))
    
    match op:
        case 1:
            cont1 += 1
        case 2:
            cont2 +=1 
        case 3:
            cont3 += 1
        

print(f"o numero total de votos do candidato 1 é de: {cont1} ")
print(f"o numero total de votos do candidato 2 é de: {cont2} ")
print(f"o numero total de votos do candidato 3 é de: {cont3} ")