#  Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: 

# a.	Mostre a quantidade de valores que foram lidos; 
# b.	Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
# c.	Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
# d.	Calcule e mostre a soma dos valores; 
# e.	Calcule e mostre a média dos valores; 
# f.	Calcule e mostre a quantidade de valores acima da média calculada; 
# g.	Calcule e mostre a quantidade de valores abaixo de sete; 
# h.	Encerre o programa com uma mensagem.


valores = []
valores2 = []
soma = 0
medias = []

while True:
    num = float(input("informe sua nota: "))
    valores.append(num)
    valores2.insert(0, num)
    

    soma = num + soma
    media = sum(valores) / len(valores)
    medias.append(media)
    

    if num == -1:
        print(f"os valors lidos foram: {valores}")
        print(f"os valores lidos em ordem inversa: {valores} ")
        print(f"a soma dos valores é de: {soma} ")
        print(f"a media dos valores é de: {media} ")
        if media > 7:
            print(f"a quantidade de valores acima da media são: {media}")