usuario = {}
filmes = {
    "Jonga o Filme": [12, "22:00", 40.25, '+30', 2],
    "Amongus assassino e REAL(ou fake?)": [10, '18;00', 50, '+16', 30],
    "Pixelmon a origem": [15, '16:30', 40.50, 'L', 40 ],
}

ingressos = {}
principal = 55

while principal != 0:
    print('selecione 1 para gerenciar filmes: ')
    print('selecione 2 para gerenciar seus ingressos: ')
    print('selecione 3 para se cadastrar: ')
    print('selecione 0 para sair do sistema: ')

    principal = input('\ndigite a opção desejada: ')

    if principal == '1':
        email = input('digite o email: ')
        senha = input('digite a senha: ')
        if not email in usuario or usuario[email][3] != senha or usuario[email][2] != '1':
            print("Login inválido")
            continue
        print('selecione 1 para buscar filme')
        print('selecione 2 para adicionar filme')
        print('selecione 3 para atualizar dados do filme')
        print('selecione 4 para remover filme')
        print('selecione 5 para ver ingressos')
        print('selecione 6 para remover ingressos')
        escolha_adm = input('\ndigite a opção desejada: ')
        if escolha_adm == '1':
            if len(filmes) < 1:
                print('nenhum filme registrado')
                continue
            index = 1
            for filme in filmes:
                print(f'{index}. - {filme}, sala: {filmes[filme][0]}, ' \
                      f'horário: {filmes[filme][1]}, valor: {filmes[filme][2]}, ' \
                      f'faixa etária {filmes[filme][3]}, capacidade: {filmes[filme][4]}')
                index += 1

        elif escolha_adm == '2':
            filme = input('nome do filme: ')
            sala = int(input('sala do filme: '))
            horario = input('horario do filme: ')
            preco = float(input('preço do filme: '))
            faixa = input('faixa etária: ')
            capacidade = float(input('Digite a capacidade da sala: '))
            filmes[filme] = [sala, horario, preco, faixa, capacidade]
            
        elif escolha_adm == '3':
            if len(filmes) < 1:
                print('nenhum filme registrado')
                continue
            filme = input('digite o nome do filme: ')           
            if not filme in filmes:
                print('filme inválido')
                continue
            print('selecione 1 para mudar o nome do filme')
            print('selecione 2 para mudar a sala do filme')
            print('selecione 3 para mudar o horário do filme')
            print('selecione 4 para mudar o preço do filme')
            print('selecione 5 para mudar a faixa do filme')
            print('selecione 6 para mudar a capacidade de sala')
            escolha_mfilme = input('\ndigite a opção desejada: ')
            if escolha_mfilme == '1':
                nome = input('digite o novo nome do filme: ')
                filmes[nome] = filmes[filme]
                del filmes[filme]
            elif escolha_mfilme == '2':
                sala = int(input('digite o novo número da sala: '))
                filmes[filme][0] = sala
            elif escolha_mfilme == '3':
                horario = input('digite o novo horário: ')
                filmes[filme][1] = horario
            elif escolha_mfilme == '4':
                preco = float(input('digite o novo preço: '))
                filmes[filme][2] = preco
            elif escolha_mfilme == '5':
                faixa = input('digite a nova faixa etária: ')
                filmes[filme][3] = faixa
            elif escolha_mfilme == '6':
                capacidade = int(input('digite a capacidade da sala: '))
                filmes[filme][4] = capacidade
            else:
                print('opção invalida')
                continue

        elif escolha_adm == '4':
            if len(filmes) < 1:
                print('nenhum filme registrado')
                continue
            filme = (input('digite o nome do filme: '))
            if not filme in filmes:
                print('filme inválido')
                continue
            del filmes[filme]

        elif escolha_adm == '5':
            if len(ingressos) < 1:
                print('nenhum ingresso registrado')
                continue
            for user in ingressos:
                print(f"{user}. - {ingressos}")
        elif escolha_adm == '6':
            if len(ingressos) < 1:
                print('nenhum ingresso registrado')
                continue
            escolha_ingresso = int(input('digite o email do usuário'))
            if not escolha_ingresso in ingressos:
                print('usuário inválido')
                continue
            print(f'removido {ingressos[escolha_ingresso]} de {escolha_ingresso}')
            del ingressos[escolha_ingresso]

        else:
            print('opção invalida')
    
    elif principal == '2':
        email = input('digite o email: ')
        senha = input('digite a senha: ')
        if not email in usuario or usuario[email][3] != senha or usuario[email][2] != '2':
            print("Login inválido")
            continue
        print('selecione 1 para comprar ingresso')
        print('selecione 2 para reembolsar ingresso')
        escolha_usr = input('\ndigite a opção desejada: ')
        if escolha_usr == '1':
            ###################################################
            index = 1
            for filme in filmes:         
                print(f'{index}. - {filme}, sala: {filmes[filme][0]}, ' \
                      f'horário: {filmes[filme][1]}, valor: {filmes[filme][2]}, ' \
                      f'faixa etária {filmes[filme][3]}, capacidade: {filmes[filme][4]}')
                index += 1
            escolha_filme = input('escolha um filme: ')
            if not escolha_filme in filmes:
                print('filme inválido')
                continue
            ocupados = 0
            for kemail in ingressos:
                if ingressos[kemail] == escolha_filme:
                    ocupados += 1
            if ocupados >= filmes[escolha_filme][4]:
                print('a sala está cheia')
                continue
            print(f"Comprado {escolha_filme}")
            ingressos[email] = escolha_filme
            
        elif escolha_usr == '2':
            if not email in ingressos:
                print('não há ingresso para reembolsar')
                continue
            print(f'reembolsado {ingressos[email]}')
            del ingressos[email]

        else:
            print('opção invalida')

    elif principal == '3':
        nome = input('digite seu nome: ')
        email = input('digite seu email: ')
        senha = input('digite sua senha: ')
        cargo = input('escolha 1 para ser adm ou 2 para usuario: ')
        if email in usuario:
            print('usuário já existe')
            continue
        usuario[email] = [email, nome, cargo , senha]
    
    elif principal == '0':
        break

    else:
        print('opção invalida')