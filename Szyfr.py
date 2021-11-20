def szyfruj(napis):
    kod = input("Chcesz użyć szyfru GADERYPOLUKI (G), POLITYKARENU (P), czy własnego (W)?")
    if kod == 'G':
        szyfr = {'G': 'A', 'D': 'E', 'R': 'Y', 'P': 'O', 'L': 'U', 'K':'I'}
    if kod == 'P':
        szyfr = {'P': 'O', "L": 'I', 'T': 'Y', 'K': 'A', 'R': 'E', 'N': 'U'}
    if kod == 'W':
        szyfr = {}
        print("Podaj szyfrujące litery. Wpisz je jako wielkie litery")
        lst1 = []
        for i in range(6):
            x = input("Podaj literę nr "+str(i+1))
            y = input("Podaj zamiennik litery nr "+str(i+1))
            szyfr[y] = x
            lst1.append(x)
            lst1.append(y)
        lst1 = sorted(lst1)
        zb = set(lst1)
        lst2 = sorted(list(zb))
        if lst1 != lst2:
            return "Szyfr nieprawidłowy"
    odwrotny = {v: k for k, v in szyfr.items()}
    szyfr = {**szyfr, **odwrotny}
    male = {k.lower(): v.lower() for k, v in szyfr.items()}
    szyfr = {**szyfr, **male}

    wyjscie = ""
    for e in napis:
        if e in szyfr:
            wyjscie += szyfr[e]
        else:
            wyjscie += e
    return wyjscie

print(szyfruj("Pewien napis"))
print(szyfruj(szyfruj("Pewien napis")))