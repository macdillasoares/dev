# Sistema de classificação de idades 
idade = 35 
if idade < 13: 
    categoria = "Criançaa" 
elif idade < 18: 
    categoria= "Adolescente" 
elif idade < 60: 
    categoria = "Adulto" 
else:
    categoria = "Idoso" 
    print(f"Idade: {idade} anos - Categoria: {categoria}") 
# Sistema de notas com conceitos 
nota = 8.5 
if nota >= 9.0: 
    conceito = "A" 
    situacao ="Excelente" 
elif nota >= 8.0: 
    conceito = "B" 
    situacao = "Muito Bom" 
elif nota >= 7.0: 
    conceito = "C" 
    situacao ="Bom" 
elif nota >= 6.0: 
    conceito = "D" 
    situacao = "Suficiente" 
else: 
    conceito = "F" 
    situacao = "Insuficiente"
print(f"Nota: {nota} - Conceito: {conceito} - {situacao}")
