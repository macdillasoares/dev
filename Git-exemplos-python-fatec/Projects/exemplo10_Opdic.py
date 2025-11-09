# Criando dicionários 
pessoa = { "nome": "João Silva", "idade": 25, "curso": "Segurança da Informação", "ativo":True }          
print("Dicionário pessoa:", pessoa) 
# Acessandovalores 
print("Nomee:", pessoa["nome"]) 
print("Idade:", pessoa.get("idade")) # Adicionando/modificando
pessoa["email"] = "joao@email.com" 
pessoa["idade"] = 26
print("Pessoa atualizada:", pessoa) # Obtendo chaves e valores 
print("Chaves:", list(pessoa.keys()))
print("Valores:", list(pessoa.values())) # Verificando se chave existe 
if "telefone" in pessoa: 
            print("Telefone:", pessoa["telefone"]) 
else:print("Telefone não cadastrado")
