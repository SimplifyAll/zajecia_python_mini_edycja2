#!/usr/bin/env python
# -*- coding: utf-8 -*-


def podzielne(start, stop, dzielnik):
    for liczba in range(start, stop):
        if liczba % dzielnik == 0:
            print liczba

podzielne(0, 10, 2)

podzielne(20, 30, 3)
