relatorio = []
def valorpagamento(prest,atraso):
    if atraso == 0:
        print(f"O valor da prestação é R${prest}")
    else:
        vf = lambda prest,atraso: (prest + prest*3/100) + atraso*(prest*1/100)
        return vf

while True:
    prest = float(input("Qual o Valor da pretação? R$"))
    if prest == 0:
        print("Fim do programa")
        print(relatorio)
        break
    else:
        atraso = int(input("Quantos dias de atraso? "))
        relatorio.append(valorpagamento(prest,atraso))
        print(valorpagamento(prest,atraso))
