


def sla():
    a = int(input("informe um numero: "))
    b = int(input("informe outro numero: "))
    limite = int(input("informe o valor do limite: "))
    if a + b > limite:
        return "true"
    else:
        return "false"

print(sla())