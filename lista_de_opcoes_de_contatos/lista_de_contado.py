# - A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# - Deve ser possível adicionar um contato
# - O contato pode ter os dados:
# - Nome
# - Email
#- Favorito (está opção é para poder marcar um contato como favorito)
#- Deve ser possível visualizar a lista de contatos cadastrados
#- Deve ser possível editar um contato
#- Deve ser possível marcar/desmarcar um contato como favorito
#- Deve ser possível ver uma lista de contatos favoritos
#- Deve ser possível apagar um contato

def adicionar_contato(contatos, nome_do_contato, numero_do_contato, email_do_contato):
  contato = {"contato": nome_do_contato, "numero": numero_do_contato, "email": email_do_contato, "favorito":False}
  contatos.append(contato)
  print(f'Contato {nome_do_contato} de número {numero_do_contato} e email {email_do_contato} foi adicionado com sucesso!')
  return

def ver_contatos(contatos):
  print('\nLista de contatos:')
  for indice, contato in enumerate(contatos, start=1):
    status = "✩" if contato['favorito'] else ''
    nome_do_contato = contato['contato']
    numero_do_contato = contato['numero']
    email_do_contato = contato['email']
    print(f"{indice}.[{status}]{nome_do_contato}, {numero_do_contato}, {email_do_contato}")
  return

def ver_contatos_favoritos(contatos):
  print('\nLista de contatos:')
  for indice, contato in enumerate(contatos, start=1):
    status = "✩" if contato["favorito"] else " "
    nome_do_contato = contato["nome"]
    numero_do_contato = contato["numero"]
    email_do_contato = contato["email"]

    if contato["favorito"]:
      print(f"{indice}.[{status}]{nome_do_contato}, {numero_do_contato}, {email_do_contato}")
  return

def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_contato, novo_email_contato):
  indice_contato_ajustado = int(indice_contato) - 1 
  if indice_contato_ajustado>= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["contato"] = novo_nome_contato

    contatos[indice_contato_ajustado]["numero"] = novo_numero_contato

    contatos[indice_contato_ajustado]["email"] = novo_email_contato

    print(f'O contato {indice_contato} foi atualizado para {novo_nome_contato}, {novo_numero_contato}, {novo_email_contato}')
  else:
    print('Indice de contato invàlido.')
  return

def favoritar_contato(contatos, indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  contatos[indice_tarefa_ajustado]["favorito"] = True
  print(f"Contato {indice_tarefa} marcada como favorito")
  return

def deletar_contato(contatos, indice_contato): # a consertar 
  indice_contato_ajustado = int(indice_contato) - 1 
  # https://awari.com.br/lista-python-remova-um-item-facilmente/#:~:text=Uma%20das%20formas%20mais%20simples,com%20base%20no%20seu%20valor.
  #del(contatos[indice_contato])
  contatos.pop(indice_contato_ajustado)
  print('O contato foi removido')
  return 

 
contatos = []

while True:
  print("\nMenu do Gerenciador de Lista de contato:")
  print("1. Adicionar contato")
  print("2. Ver contato")
  print("3. Ver contato favoritos")
  print("4. Atualizar contato")
  print("5. favoritar contatos")
  print("6. Deletar contato")
  print("7. Sair")
  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_do_contato = input("Digite o nome de contato que deseja adicionar: ")

    numero_do_contato = input("Digite o número de contato que deseja adicionar: ")

    email_do_contato = input("Digite o email de contato que deseja adicionar: ")
    #if len(numero_do_contato) == (8 or 9) and len(nome_do_contato) != 0:
    adicionar_contato(contatos, nome_do_contato, nome_do_contato, email_do_contato )
    #else:
     # print('A quantidade de números é insuficiente, tente novalmente')

  elif escolha == "2":
    ver_contatos(contatos)
  
  elif escolha == "3":
    ver_contatos_favoritos(contatos)
  
  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite o indice de contato que deseja editar: ")
    novo_nome = input("Digite o novo nome de contato:")
    novo_numero = input("Digite o novo nome de contato:")
    novo_email = input("Digite o novo email de contato:")
    atualizar_contato(contatos, indice_contato, novo_nome, novo_numero, novo_email)
  
  elif escolha =="5":
    ver_contatos(contatos)
    indice_contato = input("Digite o número da contato que deseja favoritar: ")
    favoritar_contato(contatos, indice_contato)

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input("Digite o indice do contato que deseja deletar: ")
    deletar_contato(contatos, indice_contato)
    ver_contatos(contatos)

  elif escolha == "7":
    break

print("Programa finalizado")