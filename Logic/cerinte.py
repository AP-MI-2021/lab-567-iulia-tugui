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


