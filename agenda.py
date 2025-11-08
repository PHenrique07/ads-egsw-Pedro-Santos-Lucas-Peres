agenda = {}

def adicionar_compromisso():
    data = input("Digite a data (dd/mm/aaaa): ")
    compromisso = input("Digite o compromisso: ")

    if data in agenda:
        agenda[data].append(compromisso)
    else:
        agenda[data] = [compromisso]

    print("Compromisso adicionado com sucesso!")

def ver_agenda():
    if not agenda:
        print("A agenda está vazia.")
        return

    for data, compromissos in agenda.items():
        print(f"\nData: {data}")
        for c in compromissos:
            print(f"- {c}")

def remover_compromisso():
    data = input("Digite a data do compromisso a remover (dd/mm/aaaa): ")

    if data in agenda:
        print(f"\nCompromissos em {data}:")
        for i, c in enumerate(agenda[data], start=1):
            print(f"{i}. {c}")
        escolha = int(input("Digite o número do compromisso que deseja remover: "))

        if 1 <= escolha <= len(agenda[data]):
            removido = agenda[data].pop(escolha - 1)
            print(f"Compromisso '{removido}' removido com sucesso!")
            if not agenda[data]:
                del agenda[data]
        else:
            print("Número inválido.")
    else:
        print("Data não encontrada na agenda.")

def contar_compromissos():
    """Função nova: mostra o total de compromissos na agenda."""
    total = sum(len(compromissos) for compromissos in agenda.values())
    print(f"Total de compromissos registrados: {total}")

def menu():
    while True:
        print("\n--- SISTEMA DE AGENDA ---")
        print("1. Adicionar compromisso")
        print("2. Ver agenda completa")
        print("3. Remover compromisso")
        print("4. Contar compromissos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_compromisso()
        elif opcao == "2":
            ver_agenda()
        elif opcao == "3":
            remover_compromisso()
        elif opcao == "4":
            contar_compromissos()
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
