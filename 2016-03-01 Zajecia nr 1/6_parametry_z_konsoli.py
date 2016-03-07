#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def podzielne(start, stop, dzielnik):
    for liczba in range(start, stop):
        if liczba % dzielnik == 0:
            print liczba

podzielne(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
