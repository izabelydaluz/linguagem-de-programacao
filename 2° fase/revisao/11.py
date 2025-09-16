#11
cods = []
acidentes = []
passeios = []
geral = {}
geral2 = []

i=0
while i < 2:
    i += 1
    cod = int(input("informe o codigo da cidade:"))
    cods.append(cod)
    passeio =  int(input("informe o numero de veiculos de passeio (em 1999): "))
    passeios.append(passeio)

    acidente = int(input("informe o numero de acidentes de transito (em 1999):" ))
    acidentes.append(acidente)

    geral['cod'] = cod
    geral['passeio'] = passeio
    geral['acidente'] = acidente
    geral2.append(geral)

print(f"o maior indice de acidentes é de: {[max(acidentes)]}")
print(f"o menor indice de acidentes é de:{[min(acidentes)]}")

media = sum(passeios)/len(passeios)

print(f"a media das 5 juntas é de : {media}")

for v in geral2:
    if passeio < 2000:
        media2 = sum(acidentes)/len(acidentes)
        print(f"a media com menos de 2000 de passeio é de:{media2}")