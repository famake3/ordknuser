alle = [o.lower() for o in
        open("ordliste_aspell.txt", "rb")
                .read().decode('latin1').splitlines()
        if o.isalnum() and (len(o) >= 2 or o in ["åi"]) and
            sum(1 for x in o if not x.islower()) < 2
        ]

fast_ord = "cubastolen"
mollengde = len(fast_ord)*2-1 # Kan endres
print("Antall ord:", len(alle))

def sjekke(antall, forklar, prefisk, fastord_igen, gjenstende, fo_offset):
    for ordet in alle:
        ord_leng = len(ordet)
        if ord_leng > gjenstende:
            continue
        if all(a == b for (a, b) in zip(ordet[fo_offset::2], fastord_igen)):
            prefisk2 = prefisk + ordet
            forklar2 = forklar + ("." + ordet)
            fastord_igen2 = fastord_igen[(ord_leng+1-fo_offset)//2:]
            gjenstende2 = gjenstende - ord_leng
            fo_offset2 = (ord_leng + fo_offset) % 2
            if gjenstende2 == 1 and fo_offset2 == 0:
                prefisk2 += fastord_igen2[-1]
                forklar2 += (":" + fastord_igen2[-1])
                gjenstende2 = 0
            if gjenstende2 == 0:
                print(antall, forklar2)
            elif gjenstende2 > 0:
                sjekke(antall+1, forklar2, prefisk2, fastord_igen2, gjenstende2, fo_offset2)

sjekke(0, "", "", "cubastolen", len("cubastolen")*2-1, 0)
sjekke(0, "", "", "cubastolen", len("cubastolen")*2, 1)
sjekke(0, "", "", "cubastolen", len("cubastolen")*2+1, 1)

