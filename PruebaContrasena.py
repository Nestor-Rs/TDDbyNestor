import Generador

#Prueba de Mayuscula
def Mayuscula(f,Longi):
    Passe=False
    cadena = f(Longi)
    for i in range(Longi):
        if ord(cadena[i])<91 and ord(cadena[i])>64:
            Passe = True
            break;
        else:
            Passe = False
    return Passe

#Prueba de Minuscula
def Misnucula(f,Longi):
    Passe=False
    cadena = f(Longi)
    for i in range(Longi):
        if ord(cadena[i])<123 and ord(cadena[i])>96:
            Passe=True
            break;
        else:
            Passe=False
    return Passe
#Prueba de Numero
def Numero(f,Longi):
    Passe=False
    cadena = f(Longi)
    for i in range(Longi):
        if ord(cadena[i])<58 and ord(cadena[i])>47:
            Passe=True
            break;
        else:
            Passe=False
    return Passe

print(Mayuscula(Generador.ContraG,6))
print(Misnucula(Generador.ContraG,6))
print(Numero(Generador.ContraG,6))
