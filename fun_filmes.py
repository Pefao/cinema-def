from fun_sala import *
import re
filmes = []
validador_horario = re.compile("^([01]\\d|2[0123]):[012345]\\d$")
validador_valor = re.compile("^\\d+([\\.,]\\d{1,2})?$")
def adm_menu_filmes():
    print("\033[34m--------Cadastre o Filme--------\033[0m")
    while True:
        nome_filme = input("\nDigite o nome do filme: ")
        sala_procura = input("selecione a sala: ")
        sala = None
        for sala2 in salas:
            if sala_procura == sala2["sala"]:
                sala = sala2["sala"]
                break
        if sala == None:
            print("\033[31msala invalida\033[0m")
            continue
        horario = input("Digite o Horario: ")
        if not validador_horario.match(horario):
            print("\033[31mhorario invalido\033[0m")
            continue
        valor = input ("digite o Valor: ")
        if not validador_valor.match(valor):
            print("\033[31mvalor invalido\033[0m")
            continue
        break 

    filme = {
        "nome_filme" : nome_filme,
        "sala" : sala,
        "horario" : horario,
        "valor" : valor,
    }
    
    filmes.append(filme)
    print("\033[32mFilme cadastrado com sucesso!\033[0m")

#-------------------------------------------------------------------------------------------------------------------------    
def list_filmes():
    for filme in filmes:
        print(f"-----Filme-----\n{filme['nome_filme']}")
        print(f"-----sala-----\n{filme['sala']}")
        print(f"-----horario-----\n{filme['horario']}")
        print(f"-----valor-----\n{filme['valor']}\n")
        
#------------------------------------------------------------------------------------------------------------------------
def edit_filme():
    print("\n\033[34m--------Area de edição de filmes--------\033[0m")
    indice = None
    while True:
        escolha_filme = input(("Digite o filme que deseja editar: "))
        for i,filme in enumerate(filmes):
            if escolha_filme == filme["nome_filme"]:
                indice = i
        if indice == None:
            print("\033[31mFilme invalido\033[0m")
            continue
        
        escolha_edit = input("Digite 1 para editar filme\nDigite 2 para editar sala \nDigite 3 para editar horario\nDigite 4 para editar valor\nDigite 5 para remover filme\nDigite 6 para sair da edição:  ")
        
        if escolha_edit == "1":
            edit_filme = input("Digite o novo nome do filme: ")
            filmes[indice]["nome_filme"] = edit_filme
            print("\033[32mnovo filme editado com sucesso!\033[0m")
            break
        
        elif escolha_edit == "2":
            edit_sala = input("Digite a nova sala: ")
            filmes[indice]["sala"] = edit_sala
            print("\033[32mnova sala editado com sucesso!\033[0m")
            break
        
        sala_procura = input("selecione a sala: ")
        sala = None
        for sala2 in salas:
            if sala_procura == sala2["sala"]:
                sala = sala2["sala"]
                break
        if sala == None:
            print("\033[31msala invalida\033[0m")
            continue
        
        elif escolha_edit == "3":
            edit_horario = input("Digite o novo horario: ")
            if not validador_horario.match(edit_horario):
                print("\033[31mhorario invalido\033[0m")
                continue
            filmes[indice]["horario"] = edit_horario
            print("\033[32mnovo horario editado com sucesso!\033[0m")
            break
        
        elif escolha_edit == "4":
            edit_valor = input("Digite a nova sala: ")
            if not validador_valor.match(edit_valor):
                print("\033[31mvalor invalido\033[0m")
                continue
            filmes[indice]["valor"] = edit_valor
            print("\033[32mnovo valor editado com sucesso!\033[0m")
            
        elif escolha_edit == "5":
            remover_filme = input("escolha o filme que deseja remover: ")
            indice = None
            for i,filme in enumerate(filmes):
                if remover_filme == filme["nome_filme"]:
                    indice = i
                    break
            if indice is None:
                print("\033[31mFilme não encontrado.\033[0m")
                continue
                    
            certeza = input("tem certeza que deseja remover o filme? Digite sim ou não: ")
            if certeza.lower() == "sim":
                del filmes[i]
                print("\033[32mFilme removido com sucesso!\033[0m")
                break
            else:
                print("\033[31mRemoção cancelada.\033[0m")
                break


