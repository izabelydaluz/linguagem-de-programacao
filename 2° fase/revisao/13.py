#13


lista = []


while True:
    print("informações:\n1-adicionar\n2-remover\n3-exibir\n4-pesquisar\n5-sair")
    op = int(input(" informe a sua opição: "))
    match op:
        case 1:
            item = input("informe seu item: ")
            lista.append(item)
            print(lista)

        case 2: 
            print("-----------ATENÇÃO------------")
            print("deseja excluir?\n1-item")
            r = int(input("informe sua resposta: "))
            if r == 1:
                    lista.remove(item)
            
        case 3:
              print(lista)

        case 4: 
            print("informe qual deseja pesquisar:1- item")
            op3 = input("respota: ") 

            if op3 == "1": 
                item_a = input("informe o item:") 

            for item_a in lista:
                    if item_a in lista: 
                        print("item já cadastrado")
                    else: 
                        print("item não encontrado") 

        case 5:
              print("----------programa encerado----------")
              break
                   