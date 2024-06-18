menu = """
    ========= MENU =========
    Selecione uma opção:
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Sair
    ==> """
saldo = 0
LIMITE_SAQUES = 3
LIMITE = 500
extrato = ""
numero_saques = 0

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print("Operação falhou! Saldo insuficiente.") 
        elif valor_saque > 500:
            print("Operação falhou! Excedeu o limite de saque.") 
        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R${valor_saque:.2f}\n"
            print("Saque realizado!")

    elif opcao == 3:
        print(f"=========EXTRATO=========\n")
        print(f"Não foram realizadas movimentações.\n") if not extrato else print(f"{extrato}")
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == 4:
        break
    else: print("Opção inválida!")
