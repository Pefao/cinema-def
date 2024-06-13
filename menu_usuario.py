from criar_banner import *
from fun_filmes import *
from fun_cadastro import *
import re
ingressos = []
validador_saldo = re.compile("^\\d+([\\.,]\\d{1,2})?$")
def user_menu():
    print("\033[34m---------Menu de Usuario---------\033[0m")
    while True:
        escolher_banner = input("escolha o banner: ")
        filme = None
        for filme2 in banners:
            if escolher_banner == filme2["filme"]:
                filme = filme2["filme"]
                break
        if filme == None:
            print("\033[31mbanner invalida\033[0m")
            continue
        for banner in banners:
            if escolher_banner in banner["filme"]:
                print("\033[32mvoce escolheu o banner!\033[0m\n")
                print(f"-----Filme-----\n{banner['filme']}")
                print(f"-----Genero-----\n{banner['genero']}")
                print(f"-----Faixa etaria-----\n{banner['fax_etaria']}\n") 
        break


def usr_saldo():
    while True:
        add_saldo = input("\nQuanto de saldo deseja adicionar? ")
        if not validador_saldo.match(add_saldo):
            print("\033[31mSaldo invalido\033[0m")
            continue

        print("\033[32mSaldo adicionado com sucesso!\033[0m")
        break
    usuarios[indice_usuario_atual]["saldo"] = str(float(usuarios[indice_usuario_atual]["saldo"].replace(",",".")) + float(add_saldo.replace(",",".")))
    
def comprar_ingresso():
    if not filmes:
        print("\033[31mNenhum filme cadastrado\033[0m")
        return

    valor_ingresso = filmes[0]['valor']
    filme_selecionado = filmes[0]
    valor_ingresso = filme_selecionado['valor']
    
    while True:
        ingresso = input("\nQuantos ingressos deseja comprar? ")
        if not ingresso.isnumeric():
            print("\033[31mIngresso inválido!\033[0m")
            continue
        elif ingresso == "0":
            print("\033[31mSaldo insuficiente\033[0m")
        
        ingresso = int(ingresso)
        valor_total = ingresso * valor_ingresso
        saldo = usuarios[indice_usuario_atual]["saldo"]
        
        if saldo < valor_total:
            print(f"\033[31mSaldo insuficiente\033[0m")
            continue
        
        
        elif saldo > valor_total:
            print(f"\033[32mCompra confirmada!\033[0m")
            break
        

        

    
    ingresso = {
            "usuario": indice_usuario_atual,
            "filme": filme_selecionado["nome_filme"],
            "sala": filme_selecionado["sala"],
            "horario": filme_selecionado["horario"],
            "quantidade": ingresso,
            "valor_total": valor_total
        }
    ingressos.append(ingresso)

def list_ingressos():
    nome_arquivo = 'ingressos.txt'  
    with open(nome_arquivo, 'w') as arquivo:
        for ingresso in ingressos:
            for indice in range(ingresso['quantidade']):
                arquivo.write(f"-----Filme-----\n{ingresso['filme']}\n")
                arquivo.write(f"-----Sala-----\n{ingresso['sala']}\n")
                arquivo.write(f"-----Horario-----\n{ingresso['horario']}\n")
                arquivo.write(f"-----Valor-----\n{ingresso['valor_total']}\n")
                arquivo.write("\n")
    