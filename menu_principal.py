from fun_filmes import *
from fun_cadastro import *
from fun_sala import *
from criar_banner import *
from menu_usuario import*
import time
def main():
  print("\n\033[34m----------Bem vindo ao cinema----------\033[0m\n")
  #time.sleep(2)
  menu = 69
  while menu:
    print("Digite 1 para ir no menu ADM: ")
    print("Digite 2 para ir no menu Usuario: ")
    print("Digite 3 para se cadastrar: ")
    print("Digite 0 para sair do Cinema: ")

    menu = input("\nDigite a opção desejada: ")
    if menu == "1":
      login_usuario()
      if usuarios[indice_usuario_atual]["cargo"] == "adm":
         print("Digite 1 para criar banner:\nDigite 2 para editar banner:\nDigite 3 para adicionar filme:\nDigite 4 para editar filme:\nDigite 5 para criar sala:\nDigite 6 para voltar ao menu:")
      else:
         print("acesso negado")
         continue
      escolha_adm = input("\nDigite a opção desejada: ")

 
      if escolha_adm == "1":
          criar_banner()
          list_banner()
          continue
       
      elif escolha_adm == "2":
          edit_banner()
          list_banner()
          continue
       
      elif escolha_adm == "3":
          adm_menu_filmes()
          list_filmes()
          continue
       
      elif escolha_adm == "4":
          edit_filme()
          list_filmes()
          continue
       
      elif escolha_adm == "5":
          sala_capacidade()
          continue
       
      elif escolha_adm == "6":
          return main()

      else:
          print("\033[31mopção invalida\033[0m")
          continue
    
    elif menu == "2":
       login_usuario()
       print("Digite 1 para ver banner:\nDigite 2 para comprar ingresso:\nDigite 3 para ver lista de ingresso:\nDigite 4 para adicionar saldo:\nDigite 5 para voltar ao menu: ")
       escolha_usuario = input("\nDigite a opção desejada: ")
       if escolha_usuario == "1":
          list_banner()
          continue
       
       elif escolha_usuario == "2":
          user_menu()
          comprar_ingresso()
          continue
       
       elif escolha_usuario == "3":
          list_ingressos()
          continue
       
       elif escolha_usuario == "4":
          usr_saldo()
          continue
       
       elif escolha_usuario == "5":
          return main()
       
       else:
          print("\033[31mopção invalida\033[0m")
    
    elif menu == "3":
       cadastro_usuario()
       continue
       
    elif menu == "0":
       break
    
    else:
       print("\033[31mopção invalida\033[0m")
       continue
       



if __name__ == "__main__":
    main()

