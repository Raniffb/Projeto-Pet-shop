# Função para obter o peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Peso acima de 50kg. Digite um peso válido.")
        except ValueError:
            print("Valor inválido. Digite um valor numérico para o peso.")


# Função para obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro (c - curto, m - médio, l - longo): ")
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção inválida. Digite 'c', 'm' ou 'l'.")


# Função para obter os serviços adicionais
def cachorro_extra():
    extras = 0
    while True:
        print("Escolha o serviço adicional:")
        print("1 - Cortar unhas (R$10)")
        print("2 - Escovar os dentes (R$12)")
        print("3 - Limpar as orelhas (R$15)")
        print("0 - Não querer mais nada")
        try:
            opcao = int(input("Digite o número do serviço adicional: "))
            if opcao == 0:
                return extras
            elif opcao == 1:
                extras += 10
            elif opcao == 2:
                extras += 12
            elif opcao == 3:
                extras += 15
            else:
                print("Opção inválida. Digite um número válido.")
        except ValueError:
            print("Valor inválido. Digite um número.")


# Função principal
def main():
    # Exibição de boas-vindas
    print("Bem-vindo Raniff Barroncas Silva!")

    # Obter o peso do cachorro
    base = cachorro_peso()

    # Obter o tipo de pelo do cachorro
    multiplicador = cachorro_pelo()

    # Obter os serviços adicionais
    extra = cachorro_extra()

    # Calcular o total a pagar
    total = base * multiplicador + extra

    # Exibir o valor total
    print(f"Total a pagar: R${total:.2f}")


# Executar o programa
main()