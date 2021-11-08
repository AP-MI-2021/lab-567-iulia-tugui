from Domain.vanzare import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient


def aplicareDiscount(lista):
    '''
    aplica discount pentru reducerile specificate
    :param lista: lista de vanzari
    :return: o noua lista avand vanzarile actualizate
    '''
    listaNoua = []
    for vanzare in lista:
        if getTipReducereClient(vanzare) == "silver":
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                getGenCarte(vanzare),
                getPret(vanzare) - 5/100 * getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        elif getTipReducereClient(vanzare) == "gold":
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                getGenCarte(vanzare),
                getPret(vanzare) - 10 / 100 * getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

def modificareaGenuluiPentruTitlu(titlu, gen, lista):
    '''
    functia modifica genul cartii al carui titlu este dat de catre utilizator
    :param titlu: titlul cartii al carui gen se modifica
    :param gen: noul gen
    :param lista: lista de vanzari
    :return: lista de vanzari modificata
    '''
    listaNoua = []
    for vanzare in lista:
        if getTitluCarte(vanzare) == titlu:
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                gen,
                getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

def listaGenuri(lista):
    '''
    functia returneaza lista de genuri din lista de vanzari
    :param lista: lista de vanzari
    :return: lista de genuri
    '''
    listaNoua = []
    for vanzare in lista:
        gen = getGenCarte(vanzare)
        if gen not in listaNoua:
            listaNoua.append(gen)
    return listaNoua

def pretMinimPentruFiecareGen(lista):
    '''
    functia determina pretul minim pentru fiecare gen din lista de vanzari
    :param lista: lista de vanzari
    :return: lista de preturi minime
    '''
    listaNoua = listaGenuri(lista)
    listaPreturi = []
    for i in listaNoua:
        minim = None
        for vanzare in lista:
            gen = getGenCarte(vanzare)
            pret = getPret(vanzare)
            if gen == i:
                if minim == None:
                    minim = pret
                elif pret < minim:
                    minim = pret
        listaPreturi.append(minim)
    return listaPreturi

def ordonareCrescatorDupaPret(lista):
    '''
    functia ordoneaza crescator vanzarile in functie de pret
    :param lista: lista de vanzari
    :return: lista ordonata
    '''
    return sorted(lista, key=getPret)

def listaTitluriPentruFiecareGen(gen, lista):
    '''
    returneaza o lista cu titlurile cartilor care au un gen dat
    :param gen: genul pentru care se cer titlurile
    :param lista: lista de vanzari
    :return: lista cu tilurile cartilor care au un anumit gen
    '''
    listaTitluri = []
    for vanzare in lista:
        if getGenCarte(vanzare) == gen:
            if getTitluCarte(vanzare) not in listaTitluri:
                listaTitluri.append(getTitluCarte(vanzare))
    return listaTitluri


def afisareNumarTitluriDistincte(lista):
    '''
    functia returneaza o lista cu numarul de titluri distincte pentru fiecare gen
    :param lista: lista de vanzari
    :return: lista cu numarul de titluri distincte pentru fiecare gen
    '''
    listaGen = listaGenuri(lista)
    listaNumarTitluri = []
    for i in listaGen:
        listaNumarTitluri.append(len(listaTitluriPentruFiecareGen(i, lista)))
    return listaNumarTitluri

def Undo(lista, undolist, redolist):
    if len(undolist)>0:
        redolist.append(lista)
        lista = undolist.pop()
    else:
        return None
    return lista

def Redo(lista, undolist, redolist):
    if len(redolist) > 0:
        undolist.append(lista)
        lista = redolist.pop()
    return lista


