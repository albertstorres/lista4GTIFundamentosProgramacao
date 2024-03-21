# 5 - Faça um programa para cadastro de animais silvestres. Serão 10 animais cadastrados. O programa deve
#     receber o nome do animal e perguntar em qual categoria o usuário deseja cadastrá-lo 
#     (use listas, uma para cada categoria): 
#     1 - Réptil;
#     2 - Mamífero;
#     3 - Ave;
#     4 - Outro.
#     Por fim, o programa deve exibir as quatro listas e informar a quantidade de animais de cada 
#     categoria. Segue um exemplo abaixo:

# Exemplo Entrada
# arara
# 3
# macaco
# 2
# jacaré 
# 1
# joaninha
# 4
# aranha
# 4
# cobra
# 1
# onça
# 2
# tucano
# 3
# gavião
# 3
# tartaruga
# 1

# Exemplo Saída
# Répteis: ['jacaré', 'cobra', 'tartaruga'] Quantidade: 3
# Mamíferos: ['macaco', 'onça'] Quantidade: 2
# Aves: ['arara', 'tucano', 'gavião'] Quantidade: 3
# Outros: ['joaninha', 'aranha'] Quantidade: 2

repteis = []
mamiferos = []
aves = []
outros = []

print("Digite um estpécie de animal e em seguida um núero correspondente a sua categoria:")
print()
print("1 - Répteis")
print("2 - Mamíferos")
print("3 - Aves")
print("4 - Outros")
print()

for i in range (10) :
    nome = input(f"Digite o nome do {i + 1}ª animal: ")
    categoria = int(input(f"Digite a categoria do {nome}: "))
    if categoria == 1 :
        repteis.append(nome)
    elif categoria == 2 :
        mamiferos.append(nome)
    elif categoria == 3 :
        aves.append(nome)
    elif categoria == 4 :
        outros.append(nome)

print()
print(f"Répteis: {repteis} Quantidade: {len(repteis)}")
print(f"Mamíferos: {mamiferos} Quantidade: {len(mamiferos)}")
print(f"Aves: {aves} Quantidade: {len(aves)}")
print(f"Outros: {outros} Quantidade: {len(outros)}")