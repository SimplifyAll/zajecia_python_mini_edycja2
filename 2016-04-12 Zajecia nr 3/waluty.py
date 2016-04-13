#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import matplotlib.pyplot as plt  # we use it to plot the graphs
from matplotlib import rc  # we use it to change the default font configuration
import requests


# pobieramy dane
def get_data(tick=30, base="PLN"):
    params = {'base': base, 'symbols': 'EUR,USD'}

    data = dict()  # mozna tez {}

    curr_date = datetime.date(year=2015, month=4, day=1)
    while curr_date <= datetime.date.today():
        resp = requests.get(
            'http://api.fixer.io/{}'.format(curr_date),
            params=params
        )
        resp_json = resp.json()
        # resp_json['rates'].items() = [(u'USD', 0.26485), (u'EUR', 0.24626)]
        for waluta, wartosc in resp_json['rates'].items():
            if waluta not in data.keys():  # to sie odpali tylko raz
                data[waluta] = {
                    'argumenty': list(),
                    'wartosci': list(),
                }
            data[waluta]['argumenty'].append(curr_date)
            data[waluta]['wartosci'].append(wartosc)
        curr_date = curr_date + datetime.timedelta(days=tick)
    return data


# rysujemy dane na wykresie
def draw_graph(data):
    # domyslna czcionka Bitstream Vera Sans nie musi miec polskich znakow
    rc('font', family="Arial")

    linie = list()  # uzyjemy tego do dopasowania linii wykresu do legendy
    waluty = list()  # uzyjemy tego do poprawnego oznaczenia walut w legendzie
    for waluta, dane in data.items():
        # plt.plot() zwraca liste wyrysowanych obiektow, interesuje nas zerowy
        linia = plt.plot(dane['argumenty'], dane['wartosci'])[0]
        waluty.append(waluta)
        linie.append(linia)

    plt.legend(linie, waluty)  # linie i waluty sa w tej samej kolejnosci
    plt.xlabel(u"Czas")
    plt.ylabel(u"Wartości")
    plt.title(u"Nasz piękny wykres")
    plt.show()  # dopiero teraz nasz wykres pojawi sie na ekranie

dane = get_data(tick=14)  # domyslnie jest 30, ale nadpisujemy tu przez 14

draw_graph(dane)
