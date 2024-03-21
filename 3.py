# 3 - Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade 
#     de números negativos e a soma dos números positivos.

numeros = []
total_negativos = 0
soma_positivos = 0

for i in range (10) :
    numeros.append(float(input(f"Digite o {i + 1}ª número: ")))

for numero in numeros :
    if numero < 0 :
        total_negativos += 1
    else :
        soma_positivos += numero

print(f"Total de números negativos digitados: {total_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")


