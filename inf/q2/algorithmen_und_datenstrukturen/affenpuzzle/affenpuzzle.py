import random
import math

def naechste_permutation(L):
    # bestimme den maximalen Index i mit L[i] < L[i+1]
    i = len(L)-2
    gefunden = False
    while not gefunden:
        if i < 0:
            gefunden = True
        else:
            if L[i] < L[i+1]:
                gefunden = True
            else:
                i = i-1
    if i >= 0:
        # bestimme den maximalen Index j mit L[j] > L[i]
        j = i+1
        m = j
        while j < len(L)-1:
            j = j+1
            if L[j] > L[i]:
                m = j
        j = m
        # vertausche L[i] und L[j]
        h = L[i]
        L[i] = L[j]
        L[j] = h
        # kehre die Restliste ab Position i+1 um
        i = i+1
        j = len(L)-1
        while i < j:
            h = L[i]
            L[i] = L[j]
            L[j] = h
            i = i+1
            j = j-1
    else:
        # Liste ist absteigend sortiert
        # kehre Liste um
        i = 0
        j = len(L)-1
        while i < j:
            h = L[i]
            L[i] = L[j]
            L[j] = h
            i = i+1
            j = j-1
    return L

def naechste_orientierung(L):
    i = len(L)-1
    while L[i] == 3 and i >= 0:
        i = i-1
    if i >= 0:
        L[i] = L[i]+1
        j = i+1
        while j < len(L):
            L[j] = 0
            j = j+1
    else:
        j = 0
        while j < len(L):
            L[j] = 0
            j = j+1
    return L

def initKarten(n):
    figurteile = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
    karten = []
    for i in range(n):
        # Kartenelemente erzeugen
        kartenelemente = ''
        for i in range(4):
            figurteil = figurteile[random.randint(0, 7)]
            kartenelemente = kartenelemente + figurteil
        # Karte mit verschiedenen Orientierungen erzeugen
        kartenorientierung = kartenelemente
        karte = [kartenorientierung]
        for i in range(3):
            kartenorientierung = kartenorientierung[1:] + kartenorientierung[0]
            karte = karte + [kartenorientierung]
        karten = karten + [karte]
    return karten

def erzeugeKartenFeld(K, P, O):
    # K: vorhandenen Karten
    # P: Permutation der Karten
    # O: Orientierungen der Karten
    n = int(math.sqrt(len(K)))
    kartenfeld = []
    for i in range(n):
        zeile = []
        for j in range(n):
            zeile = zeile + ['k']
        kartenfeld = kartenfeld + [zeile]
    for k in range(n*n):
        karte = P[k]
        orientierung = O[k]
        karte = K[karte][orientierung]
        i = k//n
        j = k%n
        kartenfeld[i][j] = karte
    return kartenfeld

def printKartenfeld(kartenfeld):
    print('Kartenfeld')
    n = len(kartenfeld)
    linie = 3*(n+1)*'-'
    for kartenreihe in kartenfeld:
        print(linie)
        zeile = ''
        for karte in kartenreihe:
            zeile = zeile + '| ' + karte[0] + ' '
        zeile = zeile + '|'
        print(zeile)
        zeile = ''
        for karte in kartenreihe:
            zeile = zeile + '|' + karte[3] + ' ' + karte[1]
        zeile = zeile + '|'
        print(zeile)
        zeile = ''
        for karte in kartenreihe:
            zeile = zeile + '| ' + karte[2] + ' '
        zeile = zeile + '|'
        print(zeile)
    print(linie)
    

def ueberpruefeKartenFeld(kartenfeld):
    n = len(kartenfeld)
    ok = True
    for zeile in range(n):
        for spalte in range(n-1):
            ok = ok and \
            kartenfeld[zeile][spalte][1].lower() == kartenfeld[zeile][spalte+1][3].lower() and \
            kartenfeld[zeile][spalte][1] != kartenfeld[zeile][spalte+1][3]
    for spalte in range(n):
        for zeile in range(n-1):
            ok = ok and \
            kartenfeld[zeile][spalte][2].lower() == kartenfeld[zeile+1][spalte][0].lower() and \
            kartenfeld[zeile][spalte][2] != kartenfeld[zeile+1][spalte][0]
    return ok

def affenpuzzle(n):
    K = initKarten(n*n)

    # alternativ: mit Vorgabe von Karten, z.B.:
    # vorgabe = ['abbd','AacB','Ccad','BDca']
    # K = initKarten(n*n, vorgabe)
    
    L = None # lösung
    P_start = list(range(n*n)) 
    P = P_start[:]
    endePermutationen = False
    print('los')
    gefunden = False
    zaehler = 0
    while (not endePermutationen) and (not gefunden):
        #print('neue Permutation:')
        O_start = (n*n)*[0] 
        O = O_start[:]
        endeOrientierungen = False    
        while (not endeOrientierungen) and (not gefunden):
            kartenfeld = erzeugeKartenFeld(K, P, O)
            gefunden = ueberpruefeKartenFeld(kartenfeld)
            if gefunden:
                L = kartenfeld
            #print('gefunden: ', gefunden)
            O = naechste_orientierung(O)
            endeOrientierungen = (O == O_start)
            zaehler = zaehler+1
            #print(zaehler)
            #weiter = input("weiter")
        p = naechste_permutation(P)
        endePermutationen = (P == P_start)
    return (K, L)

# Test
(K, L) = affenpuzzle(3)
print('Karten:')
print(K)
print('Lösung:')
if L == None:
    print('Es existiert keine.')
else:
    printKartenfeld(L)
