from Logic.CRUD import adaugareVanzare
from Teste.allTests import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugareVanzare("1", "Harry Potter", "fantastic", 40, "silver", lista)
    lista = adaugareVanzare("3", "Scufita Rosie", "povesti", 30, "none", lista)
    runMenu(lista)

main()