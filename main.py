chamados=[]

def abrir_chamada():
    id_chamado = len(chamados) + 1
    titulo = input("Digite Qual o Problema: ").strip()
    if not titulo:
        print("Titulo não pode ficar vazio")
        return
    descricao = input("Descrição do problema: ").strip()
    if not descricao:
        print("Descrição não pode ficar vazia ")
        return
    prioridade = input("Qual a prioridade (baixa,media,alta): \n").strip().lower()
    if prioridade not in ["baixa", "media", "alta"]:
        print("Propriedade invalida.")
        return
    print(f"Titulo: {titulo}")
    print(f"Descrição: {descricao}")
    print(f"Prioridade: {prioridade}")


    chamado = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "Status": "Aberto",
        "id": id_chamado
    }
    chamados.append(chamado)
    print(f"Chamado {id_chamado} cadastrado com sucesso!")

def encerrar_chamado():
    id_chamado = int(input("Digite o ID do chamado:"))
    for chamado in chamados:
        if chamado['id'] == id_chamado:
            
            if  chamado['Status'] == "Encerrado":
                print("Esse chamado ja está encerrado.")
                return
            chamado['Status'] = "Encerrado"
            print("Chamado encerrado!")
            return
    print("Chamado Não encontrado!")

    


def lista_chamados():
    if not chamados:
        print("Nenhum chamado registrado.")
        return
    for chamado in chamados:
        print(f"titulo: {chamado['titulo']}")
        print(f"Descrição: {chamado['descricao']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"ID: {chamado['id']}")
        print(f"Status: {chamado['Status']}")
        


while True:
    try:
        print("1 - Abrir chamada")
        print("2 - Listar chamados")
        print("3 - Encerrar chamados")
        print("4 - Sair")
        print()
        opcoes = int(input("Escolha uma das opções: "))

        if opcoes == 1:
            abrir_chamada()
        elif opcoes == 2:
            lista_chamados()
        elif opcoes == 3:
            encerrar_chamado()
        elif opcoes == 4:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Por favor, digite um número válido.")
    
