# 1 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a uma grande 
#     quantidade de organizações:
#     "Qual o melhor sistema operacional para uso em servidores?"
#          As possíveis respostas são: 
#          1 - Windows Server
#          2 - Linux
#          3 - Mac OS
#          4 - outro
#     Você foi contratado para desenvolver um programa (utilizando vetores) que leia o resultado da 
#     enquete e informe ao final o resultado da mesma. O programa deverá ler os votos até ser 
#     informado o valor 0, que encerra a entrada dos dados. Os valores referentes a cada uma das opções
#     devem ser armazenadas num vetor. Após os dados terem sido informados, o programa deverá calcular o
#     total de votos de cada um dos concorrentes.

votos = []
votos_windows = 0
votos_linux = 0
votos_mac = 0
votos_outros = 0

print("1 - Windows Server")
print("2 - Linux")
print("3 - Mac OS")
print("4 - OUTROS")
print("0 - FINALIZAR")
print()

while True :
    voto = int(input("Digite o seu voto: "))
    if voto == 0 :
        print("Finalizando...")
        break
    else :
        votos.append(voto)

for voto in votos :
    if voto == 1 :
        votos_windows += 1
    elif voto == 2 :
        votos_linux += 1
    elif voto == 3 :
        votos_mac += 1
    elif voto == 4 :
        votos_outros += 1

print()
print(f"Votos Windows Server: {votos_windows}")
print(f"Votos Linux: {votos_linux}")
print(f"Votos Mac OS: {votos_mac}")
print(f"Votos Outros: {votos_outros}")
        
