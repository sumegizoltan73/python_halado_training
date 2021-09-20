
# list comprehensions 1. - lista megértések 1.

# szamok = []
# for i in range(20):
#     szamok.append(i)

szamok = [x for x in range(20)]
print(szamok)

paros = [x for x in range(20) if x % 2 == 0]
print(paros)

paratlan = [x for x in range(20) if x % 2 != 0]
print(paratlan)

nevek = ["andi", "enikő", "zsofi", "erika", "anikó"]
print(nevek)
nevek = [nev.capitalize() for nev in nevek]
print(nevek)

nevek_A = [nev for nev in nevek if nev.startswith("A")]
print(nevek_A)

