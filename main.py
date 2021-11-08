from Logic.CRUD import adaugareVanzare
from Teste.allTests import runAllTests
from UI.console import runMenu
from UI.cli import runCli


def main():
    runAllTests()
    lista = []
    option = input("Introduceti cli pentru sau ui pentru user interface: ")
    while True:
        if option == "ui":
            runMenu(lista)
            break
        elif option == "cli":
            runCli(lista)
            break
        else:
            print("Optiunea nu exista!")


main()