# 12.Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde à altura): 
# • Homens: (72.7 ∗ h) − 58 
# • Mulheres: (62, 1 ∗ h) − 44, 7

h = float(input("informe sua altura: "))
g = input("informe o seu genero[F ou M]").upper

if g == "F" :
    m = (62, 1 * h) - 44.7
    print(f" seu peso ideal deve ser{m}")
else:
    u = (72.7 * h) - 58 
    print(f"seu peso ideal deve ser: {u}")

