#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def podzielne(start=1, stop=10, dzielnik=2):
    for liczba in range(start, stop):
        if liczba % dzielnik == 0:
            print liczba

if __name__ == "__main__":
    podzielne(*sys.argv[1:])
