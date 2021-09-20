
# Anonymous Functions, Lambda expressions - Anonym-Névtelen függvények, Lambda képletek

def osszead1(a, b):
    return a+b

print(osszead1(10, 15))

osszead2 = lambda a, b: a + b
print(osszead2(25, 20))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
paros = list(filter(lambda x: x % 2 == 0, lista))
print(paros)

#for p in paros:
#    print(p)

muveletek = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b
}

# print(muveletek["add"](10, 8))
add = muveletek["add"]
print(add(12, 8))
