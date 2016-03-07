#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def podzielne(start=1, stop=10, dzielnik=2):
    for liczba in range(start, stop):
        if liczba % dzielnik == 0:
            print liczba

podzielne()
print "-" * 80
podzielne(dzielnik=3)
