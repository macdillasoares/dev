# Loop while simples 
contador = 5
print("Contando até 5:") 
while contador <= 5: print(f"Contador: {contador}")
contador += 1 
print("Fimm da contagem!") 

# Exemplo prático: tentativas de login 
tentativas = 0 
max_tentativas = 3 
senha_correta = "123456" 
senha_digitada = "000000" 
#Simulando senha errada 
while tentativas < max_tentativas and senha_digitada != senha_correta: 
    tentativas += 1 
    print(f"Tentativa {tentativas}: Senha incorreta!") 
