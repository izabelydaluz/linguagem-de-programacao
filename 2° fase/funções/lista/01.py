import math


area = lambda r: math.pi * (r ** 2)

area_r = lambda base,altura: base*altura

area_t = lambda base,altura: base*altura  

def triangulo(base,altura):
    area = base*altura/2
    return area

r = float(input("Digite o Raio: "))
print(area(r), " m")

base = float(input("Digite a Base: "))
altura = float(input("Digite a Altura: "))
print(area_r (base,altura), " m")

base = float(input("Digite a Base: "))
altura = float(input("Digite a Altura: "))
print(area_t (base,altura), " m")
