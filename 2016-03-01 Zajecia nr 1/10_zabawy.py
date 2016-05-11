#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = [10, 5, 12, 3, 4]
tupla = (666, 222, 1, 3, 4)

print bool(lista)
print bool([])

print bool(tupla)
print bool(tuple())

zbior = set((1, 5, 6, 2, 1, 5, 3))
zbior2 = set((3, 2, 1))

print zbior.union(zbior2)
print zbior.difference(zbior2)
print zbior.intersection(zbior2)

posortowana_lista = lista.sort()
print posortowana_lista
print sorted(lista)

# ponizsze nie zadziala, bo tupli nie mozna modyfikowac
# posortowana_tupla = tupla.sort()
print sorted(tupla)

slownik = {
    "foo": "bar",
    "MIMUW": "rzadzi",
    32: "hello",
}

print slownik.keys()
print slownik.values()
print slownik.items()