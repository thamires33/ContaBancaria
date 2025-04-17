class ContaBancaria:
    def __init__(self, saldo=0, limite=500, extrato="", numero_saques=0, LIMITE_SAQUES=3):
        self.saldo = saldo
        self.limite = limite
        self.extrato = extrato
        self.numero_saques = numero_saques
        self.LIMITE_SAQUES = LIMITE_SAQUES

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor < 0:
            print("Digite um valor válido")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Limite de saques excedido.")
        elif valor > self.limite:
            print("Valor do saque ultrapassou o limite.")
        else:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque realizado com sucesso. Saldo: R${self.saldo:.2f}\n")

    def depositar(self, valor):
        if valor < 0:
            print("Valor do depósito não pode ser negativo.")
        else:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso. Saldo: R${self.saldo:.2f}")

    def exibir_extrato(self):
        print("\n******* EXTRATO *********")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("*************************\n")


# Programa principal
conta = ContaBancaria()

while True:
    try:
        operacao = int(input("Qual operação deseja realizar? : \n1 - Saque\n2 - Depósito\n3 - Extrato\n4 - Encerrar sessão\n=> "))
        
        if operacao == 1:
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif operacao == 2:
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
        elif operacao == 3:
            conta.exibir_extrato()
        elif operacao == 4:
            print("Encerrando sessão.")
            break
        else:
            print("Operação inválida.")
    except ValueError:
        print("Por favor, digite um número válido.")
