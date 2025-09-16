# Crie um dicionário chamado estoque onde cada chave é o nome de
# um produto e o valor é outro dicionário com "preço" e
# "quantidade".
# O usuário pode escolher:
#  a) Adicionar produto
#  b) Atualizar quantidade
#  c) Calcular valor total do estoque
#  d) Listar todos os produtos com preço e quantidade


print('''
    -------------------------------------------------
                ESCOLHA
    a) Adicionar produto
    b) Atualizar quantidade
    c) Calcular valor total do estoque
    d) Listar todos os produtos com preço e quantidade
    ---------------------------------------------------
      
     ''' )

estoque = {"caneta":(2.50,10),"caderno":(15.00, 5),"borracha":(1.00 ,20)}

while True:
    op = input("informe sua resposta").lower()
    match op:
        case "a":
            produtonovo = input("informe um novo produto")    
            preco = float(input("informe o preco:"))
            quant = int(input("informe a quantidade")) 
        
            estoque[produtonovo] = [preco,quant]

        case "b":
            nome = input("informe o produto que deseja atualizar:")
            estoque[nome][1] =int(input("atualize a quantidade:"))
            print(estoque[nome])

        case "c":
            for v in estoque:
                quant,preco = estoque[v]
                vt += quant*preco
                print(vt)
            vt = 0
        case "d":
            print(estoque)
        case _:
            break
        


