curso = "curso de python"
nome_curso = curso
saldo, limite = 200, 200

#operador "is" compara se as variáveis ocupam a mesma identidade (posição na memória).
print (curso is nome_curso)
print (curso is not nome_curso)
print (saldo is limite)

#diferença entre "is" e "=="
x = [1, 2, 3]
y = [1, 2, 3]

#valores iguais
print(x == y)

#objetos diferentes
print(x is y)  
