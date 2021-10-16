import Calculadora
#Pruebas de Suma
def PruebaSuma(fSuma,ValorA,ValorB):
    if fSuma(ValorA,'+',ValorB) == ValorB+ValorB:
        return True
    else:
        return False
#Pruebas de Resta
def PruebaResta(f,ValorA,ValorB):
    if f(ValorA,'-',ValorB) == ValorB-ValorB:
        return True
    else:
        return False
#Pruebas de Multiplicacion
def PruebaMultiplicacion(f,ValorA,ValorB):
    if f(ValorA,'*',ValorB) == ValorB*ValorB:
        return True
    else:
        return False
#Pruebas de Division
def PruebaDivision(f,ValorA,ValorB):
    if f(ValorA,'/',ValorB) == ValorA/ValorB:
        return True
    else:
        return False

print(PruebaSuma(Calculadora.Calculadora,1,1))
print(PruebaResta(Calculadora.Calculadora,1,1))
print(PruebaMultiplicacion(Calculadora.Calculadora,2,2))
print(PruebaDivision(Calculadora.Calculadora,1,2))