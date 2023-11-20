import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='academia',
    user='root',
    password='302302')

if conexao.is_connected():
    print("Conectado ao banco de da dados com sucesso!")
    cursor = conexao.cursor()
while True:
    escolha = input(f'\n'
                    f'-----------------------\n'
                    f'---------CRIAR---------\n'
                    f'----------LER----------\n'
                    f'-------ATUALIZAR-------\n'
                    f'--------DELETAR--------\n'
                    f'-----------------------\n'
                    f'\nEscolha sua ação: ')

    if escolha == "criar" or escolha == "criar".upper():
        tabela = input("\nQual tabela deseja alterar: ")
        if tabela == "aluno" or tabela == "aluno".upper():
            nome = input("Digite o nome do aluno: ")
            endereco = input("Digite o endereço: ")
            telefone = input("Digite o telefone: ")
            insert = (f'INSERT INTO aluno(nome, endereco, telefone) '
                      f'VALUES("{nome}","{endereco}","{telefone}")')
            cursor.execute(insert)
            conexao.commit()
        else:
            print("Escolha inválida")

    elif escolha == "ler" or escolha == "ler".upper():
        tabela = input("\nQual tabela deseja visualizar: ")
        if tabela == "aluno" or tabela == "aluno".upper():
            read = f'SELECT * FROM {tabela}'
            cursor.execute(read)
            print("\nMostrando os dados")
            print("-" * 20)
            for x in cursor.fetchall():
                print(f'''
                        Id: {x[0]}
                        Nome: {x[1]}
                        Endereço: {x[2]}
                        Telefone: {x[3]}''')
            print("-" * 20)

    elif escolha == "atualizar" or escolha == "atualizar".upper():
        tabela = input("\nQual tabela deseja alterar: ")
        if tabela == "aluno" or tabela == "aluno".upper():
            opcao = input("Qual valor deseja alterar: ")
            if opcao in "nomeNOME":
                antigo_nome = input("Digite o antigo nome: ")
                novo_nome = input("Digite o novo nome: ")
                update = f'UPDATE {tabela} SET nome="{novo_nome}" WHERE nome ="{antigo_nome}"'
                cursor.execute(update)
            elif opcao in "enderecoENDERECO":
                antigo_endereco = input("Digite o antigo endereço: ")
                novo_endereco = input("Digite o novo endereço: ")
                update = f'UPDATE {tabela} SET endereco="{novo_endereco}" WHERE endereco ="{antigo_endereco}"'
                cursor.execute(update)
            elif opcao in "telefoneTELEFONE":
                antigo_telefone = input("Digite o antigo telefone")
                novo_telefone = input("Digite o novo telefone: ")
                update = f'UPDATE {tabela} SET telefone="{novo_telefone}" WHERE telefone ="{antigo_telefone}"'
                cursor.execute(update)
            else:
                print("Valor inválido.")
            conexao.commit()

    elif escolha == "deletar" or escolha == "deletar".upper():
        print("\n"
              "---Escolha com cuidado o que deseja deletar, pois---\n"
              "deletará todos os dados respectivos à tal informação.\n"
              "-------------Use por sua conta e risco.-------------".upper())
        continuar = input("\nDeseja continuar? (S/N)\n")
        if continuar in "sS":
            tabela = input("\nQual tabela deseja alterar: ")
            if tabela == "aluno" or tabela == "aluno".upper():
                delete = input("Qual animal deseja deletar? ")
                deletar = f'DELETE FROM {tabela} WHERE nome = "{delete}"'
                cursor.execute(deletar)
                conexao.commit()
    else:
        print("Valor inválido.")

    decisao = input("\nDeseja fazer outra ação? (S/N)\n")
    while decisao not in "sSnN":
        decisao = input("Valor inválido. Digite novamente: (S/N)\n")
    if decisao in "sS":
        continue
    else:
        break

conexao.close()
cursor.close()


