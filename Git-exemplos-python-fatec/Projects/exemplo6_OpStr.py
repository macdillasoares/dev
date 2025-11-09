# Operações com strings 
nome = "Joãao" 
sobrenome = "Silva"#Concatenação 
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo) # Repetição 
linha = "-" * 30 
print(linha) # Tamanho da string 
print("Tamanho do nome:", len(nome)) # Maiúscula e minúscula 
print("Maiúscula:", nome.upper())
print("Minúscula:", nome.lower()) # Substituição 
email = "joao@email.com" 
novo_email = email.replace("joao","j.silva") 
print("Novo email:", novo_email)
