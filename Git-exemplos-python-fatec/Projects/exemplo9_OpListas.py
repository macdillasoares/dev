# Criando listas 
numeros = [1, 2, 3, 4, 5] 
nomes = ["Joãao", "Maria", "Pedro"] 
mista = [1, "Python", 3.14, True]
print("Lista de números:", numeros) 
print("Lista de nomes:", nomes) 
print("Lista mista:", mista) # Acessando elementos (índice começa em 0) 
print("Primeiro número:",numeros[0]) 
print("Último nome:", nomes[-1]) #Adicionando elementos 
numeros.append(6) 
nomes.insert(1, "Ana") 
print("Números após append:", numeros)
print("Nomes após insert:", nomes) # Removendo elementos 
numeros.remove(3) 
nome_removido = nomes.pop()
print("Números após remove:", numeros) 
print("Nome removido:", nome_removido) 
print("Nomes restantes:", nomes)
