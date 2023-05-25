from funcoes import limpartela, aguardar

while True:
    limpartela()
    print('(0) Sair')
    print('(1) Incluir Aluno')
    print('(2) Mostrar Lista')
    opcao = input()
    if opcao == '0':
        break
    elif opcao == '1':
        nome = input('Nome: ')
        email = input('E-mail: ')
        print()
        arquivo = open('bd.atitus', 'a') #w write/ r read / a append
        arquivo.write(nome+' '+email+'\n')
        print()
        print('Dados Salvos')
        aguardar(2)
    elif opcao == '2':
        arquivo = open('bd.atitus', 'r')
        dados = arquivo.read()
        print(dados)
        arquivo.close()
        aguardar(5)
    else:
        print('Opcão Inválida')
        aguardar(2)