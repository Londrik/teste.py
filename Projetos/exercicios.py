# =====================================================================
# EXPLICAÇÃO DAS FUNÇÕES NATIVAS: len(), sum(), min() e max()
# =====================================================================

# Vamos usar esta lista como base para os exemplos:
numeros = [10, 20, 5, 40, 25]

# 1. len() — Abreviação de "length" (comprimento)
# Retorna a quantidade total de elementos que existem dentro da lista.
total_elementos = len(numeros)
print(f"1. len(): A lista tem {total_elementos} elementos.")  # Saída: 5

# 2. sum() — Significa "sum" (soma)
# Soma todos os valores numéricos presentes na lista.
soma_total = sum(numeros)
print(f"2. sum(): A soma de todos os números é {soma_total}.")  # Saída: 100

# 3. max() — Abreviação de "maximum" (máximo)
# Encontra e retorna o maior valor de dentro da lista.
maior_valor = max(numeros)
print(f"3. max(): O maior número da lista é {maior_valor}.")  # Saída: 40

# 4. min() — Abreviação de "minimum" (mínimo)
# Encontra e retorna o menor valor de dentro da lista.
menor_valor = min(numeros)
print(f"4. min(): O menor número da lista é {menor_valor}.")  # Saída: 5

# =====================================================================
# EXEMPLO PRÁTICO: Calculando a média com sum() e len()
# =====================================================================
# Em vez de usar um for para somar e contar, você faz direto:
media = sum(numeros) / len(numeros)
print(f"\nA média dos valores é: {media}")  # Saída: 20.0




# Passo 1 — Criar a lista vazia 
nomes = [] 

# Passo 2 — Criar um for (5 repetições)
for i in range(5): 

    # Passo 3 — Pedir o nome ao usuário 
    nome = input("Digite um nome: ") 

    # Passo 4 — Adicionar o nome na lista 
    nomes.append(nome) 

# Passo 5 — Mostrar a lista completa 
print("Lista de nomes:", nomes)



# Criando a lista inicial
frutas = ["maçã", "banana", "uva", "laranja"] 

# Removendo a fruta "uva"
frutas.remove("uva")

# Adicionando "morango"
frutas.append("morango")

# Mostrando a lista atualizada
print("Lista de frutas atualizada:", frutas)




numeros = []

# Pedindo 5 números ao usuário
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Somando todos os números usando for
soma = 0
for numero in numeros:
    soma += numero

print("A soma de todos os números é:", soma)



# Criando uma lista com 10 números
numeros = [12, 7, 9, 18, 22, 5, 30, 14, 3, 44]

print("Números pares encontrados:")
# Percorrendo a lista e verificando se é par
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        
        
# Criando a lista com 4 notas
notas = [8.5, 6.0, 7.5, 7.0]

# Calculando a média
soma_notas = sum(notas)
media = soma_notas / len(notas)

print(f"Média do aluno: {media:.2f}")

# Verificação de aprovação
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
    
    
    
# Lista de alunos cadastrados
alunos = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# Pedindo o nome para pesquisa
busca = input("Digite o nome do aluno que deseja buscar: ")

# Verificando se existe na lista (ignorando maiúsculas/minúsculas com .lower())
encontrado = False
for aluno in alunos:
    if aluno.lower() == busca.lower():
        encontrado = True
        break

if encontrado:
    print("Aluno encontrado")
else:
    print("Aluno não encontrado")
    
    
# Criando uma lista com vários números
numeros = [15, 82, 4, 23, 67, 91, 12, 45]

# Exibindo as informações usando as funções nativas
print("Quantidade total de elementos:", len(numeros))
print("Maior número da lista:", max(numeros))
print("Menor número da lista:", min(numeros))


# Criando a lista vazia
tarefas = []

# Permitindo adicionar 3 tarefas
for i in range(3):
    tarefa = input(f"Digite a {i+1}ª tarefa: ")
    tarefas.append(tarefa)

# Mostrando todas as tarefas usando for
print("\n--- Suas Tarefas ---")
for tarefa in tarefas:
    print(f"- {tarefa}")

# Removendo uma tarefa escolhida pelo usuário
remover = input("\nQual tarefa você deseja remover? ")

if remover in tarefas:
    tarefas.remove(remover)
    print("Tarefa removida com sucesso!")
else:
    print("Tarefa não encontrada na lista.")

# Mostrando a lista atualizada
print("\nLista de tarefas atualizada:", tarefas)
        
        
        
        
        
        
        
