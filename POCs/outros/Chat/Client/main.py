import requests as req

usuario = {"id": -1, "nome": '', "segredo": ''}

def autentica(nome):
    #url = "http://127.0.0.1:5000/?apikey={}&i={}".format(api_key, film_id)
    url = "http://localhost:5000/usr"
    inputParams = {"nome": nome}
    try:
        retorno = req.post(url, json = inputParams).json()
    except Exception as err:
        raise str(err)
    return retorno

def listaUsuarios():
    url = "http://localhost:5000/usr"
    try:
        retorno = req.get(url).json()
    except Exception as err:
        raise 'Erro ao listar : ' + str(err)
    return retorno

def listaMinhasMensagens():
    url = "http://localhost:5000/msg/{}".format(usuario['id'])
    try:
        inputParams = {"segredo": usuario['segredo'], "inicio": 1, "fim": 99999}
        retorno = req.get(url, params = inputParams).json()
    except Exception as err:
        raise 'Erro ao listar : ' + str(err)
    return retorno    

def enviaMsg():
    pass

while True:
    print('\nUsuario:')
    value = input()
    if (value == ''):
        continue
    try:
        usr = autentica(value)
        usuario['id'] = usr['id']
        usuario['segredo'] = usr['segredo']
        usuario['nome'] = usr['nome']

        print('\nAutenticado com sucesso...')
        break
    except Exception as err:
        print(err)
        input("Pressione Enter para continar...")
        continue

while True:
    try:
        print('\n\n\n\nOpções (Digite e pressione ENTER): \n1 - Lista de destinatários \n2 - Ver minhas mensagens \n3 - Enviar Mensagem \n4 - Sair')
        value = input('=> ')
        aux = None
        
        if value == '1':
            usuarios = listaUsuarios()['usr']
            print('\n\nID -- NOME')
            for usr in usuarios:
                print(str(usr['id']) + ' -- ' + usr['nome'])
            input("Pressione Enter para voltar...")
            continue
        elif value == '2':
            mensagens = listaMinhasMensagens()['mensagens']
        elif value == '3':
            pass            
        elif value == '4':
            print('Aplicação finalizada...')
            break        
        else:
            print('Opção inválida!')
    except Exception as inst:
        print('**** ERRO: ', inst)
        print('\n\n\n\n')