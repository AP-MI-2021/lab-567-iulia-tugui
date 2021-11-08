from Domain.vanzare import getId, creeazaVanzare

def getById(id, lista):
    '''
    gaseste o vanzare cu id-ul dat in lista
    :param id: string
    :param lista: lista de vanzari
    :return: vanzarea cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None


def adaugareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista):
    '''
    adauga o vanzare intr-o lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :param lista: lista de vanzari
    :return: o lista continand atat elementele vechi, cat si vanzarea nou adaugata
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    vanzare = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
    return lista + [vanzare]
def adaugaVanzareUndoRedo(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista, undoList, redoList):
    '''
    Adauga o vanzare in lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :param lista: lista de vanzari
    :param undoList:
    :param redoList:
    :return: Retuneaza o lista continand atat elementele vechi cat si noua vanzare
    '''

    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    vanzare = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
    undoList.append(lista)
    redoList.clear()
    return lista + [vanzare]

def stergereVanzare(id, lista):
    '''
    sterge o vanzare dintr-o lista
    :param id: id-ul vanzarii care trebuie sterse
    :param lista: lista de vanzari
    :return: lista continand vechile elemente mai putin vanzarea care a fost stearsa
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    return [vanzare for vanzare in lista if getId(vanzare) != id]

def modificareVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client, lista):
    '''
    modifica vanzarea cu id-ul dat dintr-o lista
    :param id: string
    :param titlu_carte: string
    :param gen_carte: string
    :param pret: float
    :param tip_reducere_client: string
    :param lista: o lista de vanzari
    :return: lista modificata
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    listaNoua = []
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzareNoua = creeazaVanzare(id, titlu_carte, gen_carte, pret, tip_reducere_client)
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

