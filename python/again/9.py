# 9. Faça 4 listas:
# A. Filmes 
# B. Jogos 
# C. Livros 
# D. Esporte 

# a. Adicione no mínimo 2 itens em cada lista. 
# b. Crie uma lista das 4 listas criadas acima. 
# c. Acesse (mostrar) algum item da lista livros. 
# d. Remova um item da lista esporte. 

filmes = []
jogos = []
livros = []
esportes = []

for v in range(2):
    filme = input(f"informe o {v + 1}° item: ")
    filmes.append(filme)

    jogo = input(f"informe o {v + 1}° item: ")
    jogos.append(jogo)

    livro = input(f"informe o {v + 1}° item: ")
    livros.append(livro)

    esporte = input(f"informe o {v + 1}° item: ")
    esportes.append(esporte)

combinada = filmes + jogos + livros + esportes
print(f"a lista completa fica: {combinada}")

print(livros(0))

del esportes[(0)]
print(esportes)

  
