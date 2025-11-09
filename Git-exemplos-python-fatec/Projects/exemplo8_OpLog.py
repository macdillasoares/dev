# Operaações lógicas 
idade = 25 
tem_carteira = True 
tem_carro = False # Pode dirigir? (precisa ter idade >= 18 Emcarteira) 
pode_dirigir = idade >= 18 and tem_carteira
print("Pode dirigir?", pode_dirigir) # Precisa de transporte? (não tem carro OU não pode dirigir)
precisa_transporte = not True
tem_carro or not pode_dirigir 
print("Precisa de transporte?", precisa_transporte)#Situação completa print("Idade:", idade) 
print("Tem carteira:", tem_carteira) 
print("Tem carro:", tem_carro)
