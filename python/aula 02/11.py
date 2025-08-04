# 11.Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão

temp = input("olá gostaria de passar uma temperatura de [1-Fahrenheit(F) para Celsius(C)]\n ou de [2-Celsius(C) para Fahrenheit(F)]?").upper

resposta =float(input("informe o numero da temperatura para a coversão: "))

if temp == "1" :
   result = (resposta - 32) / 1,8 
   print(f"a temperatura em C é de: {result}")
else:
   result = (resposta * 1,8) + 32
   print(f"a temperatura em F é de: {result}")
