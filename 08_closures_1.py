
# clousers - bezárások 1. rész

def kulso():
    szam = 21
    def belso():
        nonlocal szam
        szam += 1
        print(szam)
    return belso

f1 = kulso()
f1()
