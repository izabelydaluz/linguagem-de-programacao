# 13.Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

n1 = float(input("informe a sua primeira nota: "))
n2 = float(input("informe a sua segunda nota: "))
n3 = float(input("informe a sua terceira nota: "))

soma = (n1+n2+n3)/3

if soma >= 6 :
    print(f"uau voce irá com media, {soma}, voce foi aprovado")
else:
    print(f"voce irá com media, {soma}... voce foi reprovado")
