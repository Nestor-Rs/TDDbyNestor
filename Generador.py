import random

def ContraG(Longi):
    Cadena=[]
    char=''
    for i in range(Longi):
        rand=random.randrange(0,3)
        if rand==0:
            char=chr(random.randrange(48,58))
            Cadena.append(char)
        elif rand==1:
            char=chr(random.randrange(65,91))
            Cadena.append(char)
        elif rand==2:
            char=chr(random.randrange(97,123))
            Cadena.append(char)
    return Cadena