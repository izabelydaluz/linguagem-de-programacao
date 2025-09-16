
def media(v1, v2, v3):
    m = (v1 + v2 + v3)/3
    if m > 6:
        return "aprovado"
    if m > 4 or m <6:
        return "Verificação Suplementar"
    if m < 4:
        return "reprovado"


v1 = float(input("informe 1° sua nota:"))
v2 = float(input("informe 2° sua nota:"))
v3 = float(input("informe 3° sua nota:"))
print(media(v1, v2, v3))
