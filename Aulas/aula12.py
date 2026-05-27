print("Questão 1:")
for numero in range(1, 11):
    print(numero)
    if numero == 6:
        break



# Questão 2: Mostre números de 1 a 10, pulando o número 5
print("\nQuestão 2:")
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)

# Questão 3: Mostre números de 1 a 20, pulando pares e encerrando no 15
print("\nQuestão 3:")
for numero in range(1, 21):
    if numero % 2 == 0:
        continue
    print(numero)
    if numero == 15:
        break

# Questão 4: Cadastro de produtos até digitar "fim"
print("\nQuestão 4:")
produtos = []
while True:
    nome = input("Digite o nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    produtos.append(nome)

print("Produtos cadastrados:")
for p in produtos:
    print(f"- {p}")

# Questão 5: Parar quando a soma chegar em 20
print("\nQuestão 5:")
soma_simples = 0
i = 1
while True:
    soma_simples += i
    if soma_simples >= 20:
        break
    i += 1
print(f"Soma atingiu: {soma_simples}")

# Atividade 6: Parada por Limite (Soma >= 50)
print("\nAtividade 6:")
total = 0
while True:
    num = float(input("Digite um número para somar: "))
    total += num
    if total >= 50:
        print(f"Limite atingido! Soma total: {total}")
        break

# Atividade 7: Sistema de Senha
print("\nAtividade 7:")
while True:
    senha = input("Digite a senha: ")
    if senha == "Teste":
        print("Acesso liberado")
        break
