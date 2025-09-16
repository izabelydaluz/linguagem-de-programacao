#14

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = []
for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / 12
print(f"\nMédia anual das temperaturas: {media_anual:.2f}°C")

print("\nMeses com temperatura acima da média anual:")

for i, temp in enumerate(temperaturas):
    if temp > media_anual:
        print(f"{i+1} - {meses[i]}: {temp:.2f}°C")
