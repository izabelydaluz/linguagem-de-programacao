#01

dinheiro  =  float(input("informe o quanto voce ganha por hora: "))
hora = float(input("informe a quantidades de horas trabalhadas"))

salario = dinheiro*hora

imposto_renda = salario*(11/100)
inss = salario*(8/100)
sindicato = salario*(5/100)

liquido = (((salario-imposto_renda)-inss)-sindicato)

print(f'o seu salario bruto é de: {salario} ')
print(f'o valor pago no INSS é de: {inss}')
print(f'o valor pago ao sindicato é de: {sindicato}')
print(f'o seu salario liquido é de: {liquido} ')

