from Domain.vanzare import creeazaVanzare, getId, getTitluCarte, getGenCarte, getPret, getTipReducereClient


def aplicareDiscount(lista):
    '''
    aplica discount pentru reducerile specificate
    :param lista: lista de vanzari
    :return: o noua lista avand vanzarile actualizate
    '''
    listaNoua = []
    for vanzare in lista:
        if vanzare['tip reducere client'] == "silver":
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitluCarte(vanzare),
                getGenCarte(vanzare),
                getPret(vanzare) - 5/100 * getPret(vanzare),
                getTipReducereClient(vanzare)
            )
            listaNoua.append(vanzareNoua)
        elif vanzare['tip reducere client'] == "gold":
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