
import random
import yagmail
import re
validar_email = re.compile("^.+@.+$")
validar_saldo = re.compile("^\\d+(.\\d{1,2})?$")
usuarios = []
indice_usuario_atual = 0

def login_usuario():
    print("\033[34m-------------login do usuario-------------\033[0m")
    while True:
        nome = input("\nDigite seu nome: ")
        usuario = None
        for idx, usuario_atual in enumerate(usuarios):
            if usuario_atual["nome"] == nome:
                usuario = usuario_atual
                break
        if usuario == None:
            print("\033[31mUsuário não encontrado!\033[0m")
            continue
        senha = input("Digite sua senha: ")
        if senha != usuario["senha"]:
            print("\033[31mSenha inválida!\033[0m")
            continue
        indice_usuario_atual = idx
        break
    

def cadastro_usuario():
    print("\033[34m-------------cadastro de usuario-------------\033[0m")
    while True:           
        nome = input("\nDigite seu nome: ")
        email = input("Digite seu email: ")
        if not validar_email.match(email):
            print("\033[31memail invalido\033[0m")
            continue
        #codigo = random.randint(10000, 99999)
        #yag = yagmail.SMTP("cinemajonga@gmail.com","tjph jwls fbup ikbc")
        #yag.send(to=email, subject="cinema do Jonga",contents=f"bem vindo ao cinema do Jonga, o seu codigo e {codigo}")
        #codigo_digitado = input("Digite o codigo de verificação: ")
        #if codigo_digitado != str(codigo):
            #print("codigo invalido")
            #continue
        senha = input("Digite sua senha: ")
        cargo = input("Digite 1 para adm e 2 para usuario: ")
        if cargo == "1":
            cargo = "adm"
        
        elif cargo == "2":
            cargo = "usuario"
        
        else:
            print("\033[31mopção invalida\033[0m")
            continue

        saldo = input("Digite seu saldo: ")
        if not validar_saldo.match(saldo):
            print("\033[31mSaldo invalido\033[0m")
            continue
        break



    usuario = {
        "nome" : nome,
        "email" : email,
        "senha" : senha,
        "cargo" : cargo,
        "saldo": saldo
    }
    usuarios.append(usuario)
    indice_usuario_atual = len(usuarios) - 1
    print("\033[32musuario cadastrado com sucesso!\033[0m")
    print(usuarios)

