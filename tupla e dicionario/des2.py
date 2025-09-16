

alunos = {"laura":(3,7,9),"monica":(7,9,8,),"alice":(2,5,6)}

for v in alunos:
    i = (sum(alunos[v]))
    if (i/3) >= 7:
        print(f"{v} aprovado")