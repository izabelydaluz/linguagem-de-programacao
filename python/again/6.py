# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. 

medias = []

for v in range(5):
    nome = input("informe seu nome: ")
    soma = 0

    for i in range(4):
        nota = float(input(f"{nome}, informe sua {i + 1}° nota: "))
        soma = nota + soma

    media = soma / 4
    medias.append(media)

aprovados = 0

if media >= 7 :
    aprovados = aprovados + 1
print(f"a quantidade de alunos foi: {aprovados}")