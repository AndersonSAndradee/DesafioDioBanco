# Função para depósito
def deposito(saldo, lista_depositos):
    valor_depositado = float(input("Digite o valor do depósito: "))
    if valor_depositado <= 0:
        print("Não é possível fazer depósito de valores negativos ou zero. Tente novamente.")
    else:
        saldo += valor_depositado
        lista_depositos.append(valor_depositado)
        print(f"O valor depositado foi {valor_depositado:.2f}. Seu saldo atual é de {saldo:.2f}")
        return saldo, lista_depositos

# Função para saque
def saque(saldo, lista_saques):
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    if valor_saque > 500:
        print("Não é permitido valores acima de 500 R$")
    elif valor_saque > saldo:
        print("Saldo insuficiente. Tente um valor menor.")
    elif valor_saque <= 0:
        print("O valor do saque deve ser positivo.")
    else:
        saldo -= valor_saque
        lista_saques.append(valor_saque)
        print(f"O valor sacado foi {valor_saque:.2f}. Seu saldo atual é de {saldo:.2f}")
        return saldo, lista_saques

# Função para visualizar extrato
def visualizar_extrato(saldo, lista_depositos, lista_saques):
    print("\nExtrato:")
    print("Depósitos:")
    for deposito in lista_depositos:
        print(f"R$ {deposito:.2f}")
    print("Saques:")
    for saque in lista_saques:
        print(f"R$ {saque:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

# Função de interface do usuário
def interface():
    saldo = 3500
    lista_depositos = []
    lista_saques = []

    while True:
        funcaoDesejada = input(" Digite que função você deseja realizar, sendo [d] p/ depósito, [s] p/ saque, [e] p/ visualizar extrato ou [q] para sair: ").lower()

        if funcaoDesejada == "d":
            if len(lista_depositos) < 3:
                saldo, lista_depositos = deposito(saldo, lista_depositos)
            else:
                print("Limite de 3 depósitos diários atingido.")

        elif funcaoDesejada == "s":
            if len(lista_saques) < 3:
                saldo, lista_saques = saque(saldo, lista_saques)
            else:
                print("Limite de 3 saques diários atingido.")

        elif funcaoDesejada == "e":
            visualizar_extrato(saldo, lista_depositos, lista_saques)

        elif funcaoDesejada == "q":
            print("Saindo...")
            break

        else:
            print("Operação inválida. Por favor, digite 'd', 's', 'e' ou 'q'.")

# Função principal
def main():
    interface()

# Chamada da função principal
main()
