#if aninhado
conta_normal = False 
conta_universitaria = True
conta_especial = False

saldo =  2000
saque = 2000
cheque_especial = 0

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
else:
    print("tipo de conta não reconhecida, contate seu gerente")
