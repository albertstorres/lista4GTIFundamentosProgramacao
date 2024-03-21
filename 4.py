# 4 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos números 
#     deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir
#     todos os vetores.

numeros = []
numeros_quadrado = []

for i in range (10) :
    numeros.append(float(input(f"Digite o {i + 1}ª número: ")))

for i in range (10) :
    numeros_quadrado.append(numeros[i] ** 2)

print(f"Vetor digitado: {numeros}")
print(f"Vetor ^2: {numeros_quadrado}")