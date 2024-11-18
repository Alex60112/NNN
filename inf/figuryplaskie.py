import math

# Sześcian
def pole_szescianu(a):
    return 6 * a**2

def objetosc_szescianu(a):
    return a**3

# Prostopadłościan
def pole_prostopadloscianu(a, b, c):
    return 2 * (a * b + b * c + a * c)

def objetosc_prostopadloscianu(a, b, c):
    return a * b * c

# Graniastosłup
def pole_graniastoslupa(Pp, Pb):
    return 2 * Pp + Pb

def objetosc_graniastoslupa(Pp, H):
    return Pp * H

# Ostrosłup
def pole_ostroslupa(Pp, Pb):
    return Pp + Pb

def objetosc_ostroslupa(Pp, H):
    return (1/3) * Pp * H

# Walec
def pole_walca(r, H):
    return 2 * math.pi * r**2 + 2 * math.pi * r * H

def objetosc_walca(r, H):
    return math.pi * r**2 * H

# Stożek
def pole_stozka(r, l):
    return math.pi * r**2 + math.pi * r * l

def objetosc_stozka(r, H):
    return (1/3) * math.pi * r**2 * H

# Kula
def pole_kuli(r):
    return 4 * math.pi * r**2

def objetosc_kuli(r):
    return (4/3) * math.pi * r**3

# Figury płaskie
def obwod_kwadratu(a):
    return 4 * a

def pole_kwadratu(a):
    return a**2

def obwod_prostokata(a, b):
    return 2 * (a + b)

def pole_prostokata(a, b):
    return a * b

def obwod_rownolegloboku(a, b):
    return 2 * (a + b)

def pole_rownolegloboku(a, h):
    return a * h

def obwod_trapezu(a, b, c, d):
    return a + b + c + d

def pole_trapezu(a, b, h):
    return (a + b) * h / 2

def obwod_trojkata(a, b, c):
    return a + b + c

def pole_trojkata(a, h):
    return 0.5 * a * h

def obwod_trojkata_rownobocznego(a):
    return 3 * a

def pole_trojkata_rownobocznego(a):
    return (a**2 * math.sqrt(3)) / 4

def obwod_kola(r):
    return 2 * math.pi * r

def pole_kola(r):
    return math.pi * r**2

def obwod_rombu(a):
    return 4 * a

def pole_rombu(a, h):
    return a * h

def pole_rombu_przekatne(e, f):
    return 0.5 * e * f

# Dodatkowe wzory
def wysokosc_trojkata_rownobocznego(a):
    return (a * math.sqrt(3)) / 2

def przekatna_kwadratu(a):
    return a * math.sqrt(2)

def twierdzenie_pitagorasa(a, b):
    return math.sqrt(a**2 + b**2)
