agenda = {}

def validar_data(data):
    """Nova função: valida se a data está no formato correto"""
    try:
        dia, mes, ano = data.split('/')
        if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
            return False
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        
        # Verifica meses válidos
        if mes < 1 or mes > 12:
            return False
            
        # Verifica dias válidos
        if dia < 1 or dia > 31:
            return False
            
        # Verifica meses com 30 dias
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
            
        # Verifica fevereiro
        if mes == 2:
            if dia > 29:
                return False
            # Verificação simples de ano bissexto
            if dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
                return False
                
        return True
    except:
        return False

def adicionar_compromisso():
    while True:
        data = input("Digite a data (dd/mm/aaaa): ")
        
        if validar_data(data):
            break
        else:
            print("Data inválida! Use o formato dd/mm/aaaa com uma data real.")
    
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