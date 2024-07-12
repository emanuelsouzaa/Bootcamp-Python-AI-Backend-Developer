"""
Emanuel Oliveira Souza
Desafio: Criando um Sistema Bancário com Python.
Bootcamp Python AI Backend Developer.
"""

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = "----- Extrato Bancário ----- \n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Quanto deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f} \n"
        else:
            print("O valor do depósito tem que ser positivo")

    elif opcao == "s":

        if numero_saques <= LIMITE_SAQUES:

            valor = float(input("Quanto deseja sacar? "))

            if valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R${valor:.2f} \n"
                else:
                    print("Você não tem saldo suficiente!")
            else:
                print("O valor por saque foi atingido!")

        else:
            print("Seu limite de saques foi atingido!")

    elif opcao == "e":

        fim_extrato = f"----- Saldo atual: R${saldo:.2f} -----"
        print(extrato + fim_extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
