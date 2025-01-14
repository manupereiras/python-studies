# IF: 
# - O comando testará a expressão lógica fornecida.
# - Se o retorno for verdadeiro, as ações no bloco de código do IF serão executadas.

saldo = 3000.0
saque = float(input("informe o valor do saque:"))

if saldo >= saque:
    print("Realizando saque!")

if saldo <= saque:
    print("Saldo insuficiente!")

# Condicional com dois desvios:
# Utiliza-se IF e ELSE.
# - Se a condição do IF for verdadeira, o bloco de código do IF será executado.
# - Caso contrário, o bloco de código do ELSE será executado.

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

# Cenários com mais de dois desvios:
# Utiliza-se o ELIF, que é uma combinação de "else if".
# Ele permite adicionar condições adicionais em uma estrutura condicional após um if.
# O ELIF só será avaliado se as condições anteriores forem falsas.

#exemplo 1
if saque <= 0:
    print("O valor do saque deve ser maior que zero.")
elif saque > saldo:
    print("Saldo insuficiente!")
else:
    saldo >= saque
    print("Saque realizado com sucesso!")

#exemplo 2
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

#if aninhado
conta_normal = False 
conta_universitaria = False
conta_especial = True

saldo =  2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com cheque especial")
    else:
        print("não foi possível realizar o saque, saldo insuficiente")

elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso")
    else:
        print("saldo insuficiente")

elif conta_especial:
    print("conta especial selecionada")
else:
    print("tipo de conta não reconhecida, contate seu gerente")
