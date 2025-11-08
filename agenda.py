# Sistema de Agenda em Python

agenda = {}

def adicionar_compromisso():
    data = input("Digite a data (dd/mm/aaaa): ")
    compromisso = input("Digite o compromisso: ")
    
    if data in agenda:
        agenda[data].append(compromisso)
    else:
        agenda[data] = [compromisso]
    
    print("Compromisso adicionado com sucesso!\n")

def listar_compromissos():
    if not agenda:
        print("Nenhum compromisso cadastrado.\n")
        return
    
    print("\nCompromissos:")
    for data, compromissos in agenda.items():
        print(f"{data}:")
        for c in compromissos:
            print(f"  - {c}")
    print()

def remover_compromisso():
    data = input("Digite a data do compromisso que deseja remover (dd/mm/aaaa): ")
    if data not in agenda:
        print("Nenhum compromisso encontrado nessa data.\n")
        return
    
    print(f"Compromissos em {data}:")
    for i, c in enumerate(agenda[data], start=1):
        print(f"{i}. {c}")
    
    try:
        indice = int(input("Digite o número do compromisso que deseja remover: "))
        removido = agenda[data].pop(indice - 1)
        print(f"Compromisso '{removido}' removido com sucesso!\n")
        
        if not agenda[data]:  
            del agenda[data]
    except (ValueError, IndexError):
        print("Opção inválida.\n")

def menu():
    while True:
        print("==== SISTEMA DE AGENDA ====")
        print("1. Adicionar compromisso")
        print("2. Listar compromissos")
        print("3. Remover compromisso")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_compromisso()
        elif opcao == '2':
            listar_compromissos()
        elif opcao == '3':
            remover_compromisso()
        elif opcao == '4':
            print("Saindo da agenda. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
