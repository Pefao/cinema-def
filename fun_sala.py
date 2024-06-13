salas = []
def sala_capacidade():
    indice = None
    while True:
        capacidade = input("\nDigite a capacidade: ")
        if not capacidade.isnumeric():
            print("\033[31mvalor invalido!\033[0m")
            continue
        sala_procura = input("Digite o numero da sala: ")
        if not sala_procura.isnumeric():
            print("\033[31msala invalida!\033[0m")
            continue
        sala_existe = False
        for sala in salas:
            if sala_procura == sala["sala"]:
                print("\033[31msala ja existe\033[0m")
                sala_existe = True
                break
        if sala_existe:
            continue
        
        break

        
            
    


            
       

    sala = {
        "capacidade" : capacidade,
        "sala" : sala_procura,
    }
    salas.append(sala)
    print(salas)