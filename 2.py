# 2 - Crie um programa que vai ler vários números e colocá-los em uma lista até que -1 seja digitado 
#     (não deve ser adicionado). Depois disso, mostre:
# a) Quantos números foram digitados;
# b) A lista de valores, ordenada de forma decrescente;
# c) Se o valor 5 está ou não na lista.

numeros = []
tem_cinco = False

print("Digite uma lista de números. \n-1 - FINALIZAR")

while True :
    numero = int(input("Digite um número: "))
    if numero == -1 :
        print("Finalizando...")
        break
    else :
        numeros.append(numero)
        if numero == 5 :
            tem_cinco = True

print(f"Foram digitados {len(numeros)} números")
print(f"Lista de números em ordem decrescente: {sorted(numeros, reverse=True)}")
if tem_cinco :
    print("O valor 5 está na lista.")
else :
    print("O valor 5 NÃO está na lista.")