def creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client):
    '''
    creeaza o vanzare
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :return: un dictionar ce retine o vanzare
    '''
    return {
        'id': id,
        'titlu carte': titlu_carte,
        'gen carte': gen_carte,
        'pret': pret,
        'tip reducere client': tip_reducere_client
    }

def getId(vanzare):
    '''
    ia id-ul vanzarii
    :param vanzare: dictionar de tipul vanzare
    :return: id-ul vanzarii
    '''
    return vanzare['id']

def getTitluCarte(vanzare):
    '''
    ia titlul cartii
    :param vanzare: dictionar de tipul vanzare
    :return: titlul cartii
    '''
    return vanzare['titlu carte']

def getGenCarte(vanzare):
    '''
    ia genul cartii
    :param vanzare: dictionar de tipul vanzare
    :return: genul cartii
    '''
    return vanzare['gen carte']

def getPret(vanzare):
    '''
    ia pretul cartii
    :param vanzare: dictionar de tipul vanzare
    :return: pretul cartii
    '''
    return vanzare['pret']

def getTipReducereClient(vanzare):
    '''
    ia tipul reducerii clientului
    :param vanzare: dictionar de tipul vanzare
    :return: tipul reducerii clientului
    '''
    return vanzare['tip reducere client']

def toString(vanzare):
    return "id: {}, titlu carte: {}, gen carte: {}, pret: {}, tip reducere client: {}".format(
        getId(vanzare),
        getTitluCarte(vanzare),
        getGenCarte(vanzare),
        getPret(vanzare),
        getTipReducereClient(vanzare)
    )

