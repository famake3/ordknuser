alle = [o.lower() for o in
        open("ordliste_aspell.txt", "rb")
                .read().decode('latin1').splitlines()
        if o.isalnum() and (len(o) >= 2 or o in ["åi"]) and
            sum(1 for x in o if not x.islower()) < 2
        ]

print("Antall ord:", len(alle))

makks_andtall_ord = 6

def dp_me(fa_stord, pre_bukkstav, post_bukkstav):
    ekspandert_ord = [c for x in fa_stord for c in (x, None)]
    if pre_bukkstav:
        ekspandert_ord = [None] + ekspandert_ord
    if not post_bukkstav:
        ekspandert_ord = ekspandert_ord[:-1]
    print("".join(c if c else '*' for c in ekspandert_ord))
    mollengde = len(ekspandert_ord)
    mulige_ord = [[list()  for i in range(mollengde+1)]
                           for j in range(mollengde)]
    for i in range(mollengde):
        for ordet in alle:
            j = len(ordet)
            if i + j <= mollengde:
                if all(a is None or a == b for (a, b) in zip(ekspandert_ord[i:], ordet)):
                    mulige_ord[i][j].append(ordet)

    beste_lol = []
    nest_beste_lol = []
    beste_antall = mollengde
    nba = mollengde
    for lQsning in reka(mulige_ord, 0, []):
        andtall = len(lQsning)
        if andtall < beste_antall:
            nest_beste_lol = beste_lol
            beste_lol = []
            nba = beste_antall
            beste_antall = andtall
        if andtall == beste_antall:
            beste_lol.append(lQsning)
        elif andtall == nba:
            nest_beste_lol.append(lQsning)

    print("Beste and:", beste_antall, ", løsninger:")
    for lQsning in beste_lol:
        print (".".join(lQsning))
    #print(" - nest beste løsninger - ")
    #for lQsning in nest_beste_lol:
    #    print (".".join(lQsning))

def reka(mulige_ord, i, funne_ord):
    if i == len(mulige_ord):
        yield funne_ord
    else:
        if len(funne_ord) < makks_andtall_ord:
            for j, oene in enumerate(mulige_ord[i]):
                for o in oene:
                    yield from reka(mulige_ord, i+j, funne_ord + [o])

def op_me(ordet):
    dp_me(ordet, False, False)
    dp_me(ordet, True, False)
    dp_me(ordet, False, True)
    dp_me(ordet, True, True)


#dp_me("cubastolen", False, False)
#dp_me("cubastolen", True, False)
#dp_me("cubastolen", True, True)
#dp_me("cubastolen", False, True)
op_me("sekvensering")

