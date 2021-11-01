from Logic.CRUD import adaugareVanzare
from Teste.allTests import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("2", "Eseu despre orbire", "fictiune", 40, "gold", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "fictiune", 30, "none", lista)
    lista = adaugareVanzare("4", "Scufita Rosie", "SF", 200, "silver", lista)
    runMenu(lista)

main()