
# iterable unpacking - iterálható objektumok kicsomagolása - list, tuple, dict, string - __iter__()

# lista1 = range(10)
# print(list(lista1))
# print(*lista1)

lista1 = [1,2,3,4]
lista2 = [*lista1]

lista2[0] = 87

print(lista1)
print(lista2)

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(10,20,30,40, **{"nev1":"Andi", "nev2":"Aniko"})

nevek = ["Andi", "Enikő", "Zsofi", "Erika", "Anikó"]
korok = [25, 28, 41, 49, 18]
nev_kor = [*nevek], [*korok]
print(nev_kor)

szoveg = "Hello! Hogy vagy?"
szoveg_lista = [*szoveg]
udv = "".join(szoveg_lista)
print(szoveg_lista)
print(udv)

