# Escreva um script em linguagem Python com uma função para imprimir o nome e salário
# de um funcionário usando as seguintes condições. Deve aceitar o nome e o salário do
# funcionário. Se o salário estiver faltando na chamada de função, atribua o valor padrão 9000
# ao salário.


def home(s):
    if s == 0 :
        s = 9000
        return s
    
while True:    
    n = input("informe seu nome: ")
    s = int(input("informe seu salario: "))
    print(home(s))

    