from Teste.testCRUD import testAdaugareVanzare, testStergereVanzare, testModificareVanzare
from Teste.testCerinte import testAplicareDiscount
from Teste.testDomain import testVanzare


def runAllTests():
    testVanzare()
    testAdaugareVanzare()
    testStergereVanzare()
    testModificareVanzare()
    testAplicareDiscount()

