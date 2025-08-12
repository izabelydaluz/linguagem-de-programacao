#13


lista = []


while True:
    print("informações:\n1-adicionar\n2-remover\n3-exibir\n4-pesquisar\n5-sair")
    op = int(input(" informe a sua opição: "))

    match op:
        case 1:
            nome = input("informe seu nome: ")
            idade= int(input("informe a sua idade: "))
            lista.append(nome)
            lista.append(idade)
            print(lista)
        case 2: 
            print("-----------ATENÇÃO------------")
            print("deseja excluir qual dos dois?\n1-nome\n2-idade")
            r = int(input("informe sua resposta: "))
            if r == 1:
                    lista.remove(nome)
            else:
                 lista.remove(idade)
        case 3:
              print(lista)

        case 4: 
            print("informe qual deseja pesquisar:\n1- nome\n2-idade")
            op3 = input("respota: ") 

            if op3 == "1": 
                nome_a = input("informe o nome:") 

            for nome_a in lista:
                    if nome_a in lista: 
                        print("nome já cadastrado")
                    else: 
                        print("nome não encontrado") 

            if op3 == "2":
                idade_a = input("informe o idade:") 
            for idade_a in lista: 
                if idade_a in lista: 
                    print("idade já cadastrado") 
                else:
                    print("idade não encontrado") 
        case 5:
              print("----------programa encerado----------")
              break
                   