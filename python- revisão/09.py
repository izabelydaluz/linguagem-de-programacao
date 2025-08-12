#09

v = 0
geral = []
f = []
m = []
while v < 4:
    v += 1
    altura = float(input("informe sua altura: "))
    geral.append(altura)

    print("sexos:\n1-feminino\n2-masculino")
    sexo = int(input("informe seu genero: "))

    match sexo:
        case 1:
            f.append(sexo)
            f.append(altura)
        case 2:
            m.append(sexo)
            m.append(altura)

for i in geral:
    print(f"a maior altura é de: {[max(geral)]}")
    print(f"a menor altura é de: {[min(geral)]}")

print(f"o numero total de homens é de:{m}")

media1 = ((len(f)/2)/4)*100
print(f"a % de mulheres é de: {media1}")

media2 = ((len(m)/2)/4)*100
print(f"a % de homens é de: {media2}")

# voltarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

