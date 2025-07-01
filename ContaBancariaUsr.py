def menu():
    menu = """\n
    MENU
    [u] Novo Usuário
    [c] Nova Conta
    [l] Listar Contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def operacoes():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando o sistema. Volte sempre!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("Falha no depósito! Valor inválido!")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, / , *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    
    # Verifica se já existe usuário com esse CPF
    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if usuario_existente:
        print("CPF já cadastrado!")
        return

    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if usuario_existente:
        usuario = usuario_existente[0]
        conta = {
            "agencia": agencia,
            "num_conta": num_conta,
            "usuario": usuario
        }
        print("Conta criada com sucesso!")
        return conta
    else:
        print("Usuário não encontrado. Não é possível criar conta.")
        return None

def listar_contas(contas):
    print("\n====== LISTA DE CONTAS ======")
    for conta in contas:
        linha = f"""\
Agência: {conta['agencia']} 
Número da Conta: {conta['num_conta']} 
Titular: {conta['usuario']['nome']}"""
        print("="*30)
        print(linha)
    if not contas:
        print("Nenhuma conta cadastrada ainda.")

if __name__ == "__main__":
    operacoes()