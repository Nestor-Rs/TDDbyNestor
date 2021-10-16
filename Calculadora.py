def Suma(ValorA,ValorB):
    return ValorA+ValorB

def Resta(ValorA,ValorB):
    return ValorA-ValorB

def Multiplicacion(ValorA,ValorB):
    return ValorA*ValorB

def Division(ValorA,ValorB):
    return ValorA/ValorB

def Calculadora(ValorA,Signo,ValorB):
    if Signo == '+':
        return Suma(ValorA,ValorB)
    elif Signo=='-':
        return Resta(ValorA,ValorB)
    elif Signo=='*':
        return Multiplicacion(ValorA,ValorB)
    elif Signo=='/':
        return Division(ValorA,ValorB)
    else:
        return None