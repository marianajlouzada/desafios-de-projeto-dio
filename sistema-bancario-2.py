def depositar(saldo, extrato, /):
    valor_deposito = float(input("Informe o valor do depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Depósito realizado!")
    else:  
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def sacar(*,saldo, extrato, LIMITE, numero_saques, LIMITE_SAQUES):
    valor_saque = float(input("Informe o valor do saque: "))
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Excedeu o limite de saques diário.") 
    elif valor_saque > saldo:
        print("Operação falhou! Saldo insuficiente.") 
    elif valor_saque > LIMITE:
        print("Operação falhou! Excedeu o limite de saque.") 
    else:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        print("Saque realizado!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print(f"=========EXTRATO=========\n")
    print(f"Não foram realizadas movimentações.\n") if not extrato else print(f"{extrato}")
    print(f"Saldo: R$ {saldo:.2f}")
    print(f"=========================\n")

def criar_usuário(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Esse CPF já está cadastrado!")
        return
    else:
        nome = input("Informe seu nome completo: ")
        data_de_nascimento = input("Informe sua data de nascimento(dd/mm/aaaa): ")
        endereco = input("Informe seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, a conta não pode ser criada!")


menu = """
    ========= MENU =========
Selecione uma opção:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Nova conta
    [5] Novo usuário
    [6] Sair
    ==> """
saldo = 0
LIMITE_SAQUES = 3
LIMITE = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
AGENCIA = "0001"
numero_conta = 1

while True:
    opcao = int(input(menu))
    if opcao == 1:
        saldo, extrato = depositar(saldo,extrato)
    elif opcao == 2:
        saldo, extrato, numero_saques = sacar(saldo= saldo, extrato=extrato, LIMITE=LIMITE, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    elif opcao == 3:
         exibir_extrato(saldo, extrato= extrato)
    elif opcao == 4:
        conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
            numero_conta += 1
    elif opcao == 5:
        criar_usuário(usuarios)
    elif opcao == 6:
        break
    else: 
        print("Opção inválida!")
