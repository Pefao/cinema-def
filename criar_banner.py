import re
valid_faixa_etaria = re.compile("^(\\+(\\d{1,3}))|(\\d{1,3}\\+)$")
valid_genero = re.compile("^[A-Za-zÀ-ÖØ-öø-ÿ\\s-]+$")
banners = []

def criar_banner():
    print("\n\033[34mCrie o banner!\033[0m\n")
    while True:
        filme = input("Digite o nome do filme do banner: ")
        genero = input("Digite o gênero do filme: ")
        if not valid_genero.match(genero):
            print("\033[31mGenero invalido\033[0m")
            continue
        fax_etaria = input("Digite a faixa etária do filme: ")
        if not valid_faixa_etaria.match(fax_etaria):
            print("\033[31mFaixa etária inválida.\033[0m")
            continue
        break
    banner = {
        "filme": filme,
        "genero": genero,
        "fax_etaria": fax_etaria
    }
    banners.append(banner)
    print("\033[32mBanner cadastrado com sucesso!\033[0m")
    
#-------------------------------------------------------------------------------------------------------------------
def edit_banner():
    print("\n\033[34m----------Area de edição de banner----------\033[0m\n")
    indice = None
    while True:
        escolha_filme = input(("Digite o filme do banner que deseja editar: "))
        for i,banner in enumerate(banners):
            if escolha_filme == banner["filme"]:
                indice = i
        if indice == None:
            print("\033[31mFilme invalido\033[0m")
            continue
        escolha_edit = input("Digite 1 para editar filme\nDigite 2 para editar genero \nDigite 3 para editar faixa etaria:\nDigite 4 para remove baner: ")
        
        if escolha_edit == "1":
            edit_filme = input("Digite o novo nome do filme: ")
            banners[indice]["filme"] = edit_filme
            print("\033[32mnovo filme editado com sucesso!\033[0m")
            break
        
        elif escolha_edit == "2":
            edit_genero = input("Digite o gênero do filme: ")
            if not valid_genero.match(edit_genero):
                    print("\033[31mGenero invalido\033[0m")
                    continue
            banners[indice]["genero"] = edit_genero
            print("\033[32mNovo genero editado com sucesso!\033[0m")
            break
        
        elif escolha_edit == "3":
            edit_fax_etaria = input("Digite a nova faixa etária do filme: ")
            if not valid_faixa_etaria.match(edit_fax_etaria):
                print("\033[31mFaixa etária inválida.\033[0m")
                continue
            banners[indice]["fax_etaria"] = edit_fax_etaria
            print("\033[32mNova faixa etaria editada com sucesso!\033[0m ")
            break
        
        elif escolha_edit == "4":
            remover_banner = input("escolha o banner que deseja remover: ")
            indice = None
            for i,banner in enumerate(banners):
                if remover_banner == banner["filme"]:
                    indice = i
                    break
            if indice is None:
                print("\033[31mbanner não encontrado.\033[0m")
                continue
                    
            certeza = input("tem certeza que deseja remover o banner? Digite sim ou não: ")
            if certeza.lower() == "sim":
                del banners[i]
                print("\033[32mbanner removido com sucesso!\033[0m")
                break
            else:
                print("\033[31mRemoção cancelada.\033[0m")
                break

        else:
            print("\033[31mnumero invalido!\033[0m")
            break

    
#---------------------------------------------------------------------------------------------------
def list_banner():
    for banner in banners:
        print(f"-----Filme-----\n{banner['filme']}")
        print(f"-----Genero-----\n{banner['genero']}")
        print(f"-----Faixa etaria-----\n{banner['fax_etaria']}\n")     