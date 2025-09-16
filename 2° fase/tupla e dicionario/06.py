#06

estoque = {"caneta":(2.50,10),"caderno":(15.00, 5),"borracha":(1.00 ,20)}

print("escolha um produto:\n1-caneta\n2-caderno\n3-borracha")
nome = input("informe o produto de seu interesse:").lower()
preco, quantidade = estoque[nome]
total = preco* quantidade
print(f"o total em estoque de {nome} é de {total}")
