saldo = 1000
saque = 200
limite = 100
contatos_emergencia = []
conta_especial = False

#operador "and"
print (saldo >= saque and saque <= limite)

#operador "or"
print (saldo >= saque or saque <= limite)

#operador "not" (inversão)
print (not 1000 > 1500)
print (not contatos_emergencia) #lista vazia em python é considerado falso
print (not "saque 1500;") #a string é verdadeira por ter valor
print (not "") #a string vazia é falsa

#operador "parênteses"
print ((saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque))

#