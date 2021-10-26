from Teste.testCRUD import testAdaugareVanzare, testStergereVanzare, testModificareVanzare, testGetById
from Teste.testCerinte import testAplicareDiscount
from Teste.testDomain import testVanzare


def runAllTests():
    testVanzare()
    testAdaugareVanzare()
    testStergereVanzare()
    testModificareVanzare()
    testAplicareDiscount()
    testGetById()

