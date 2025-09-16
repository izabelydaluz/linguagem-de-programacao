#02

temp =  float(input("informe a temperatura atual em celcius: "))


print("deseja mudar para qual temperatura??\n" \
"1-kelvin\n2- réaumur\n3- fahrenheit")
op = int(input("informe qual a opção escolhida: "))

match op :
    case 1:
        k = temp + 273.15
        print(f"a temperatura em kelvin é de : {k}")
    case 2:
        re = temp * 0.8
        print(f"a temperatura em réaumur é de : {re}")
    case 3:
        f = temp * 1.8 + 32
        print(f"a temperatura em fahrenheit é de : {f}")

