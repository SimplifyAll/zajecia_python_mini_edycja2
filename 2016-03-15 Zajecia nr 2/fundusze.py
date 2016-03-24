#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import python core library modules first
from collections import OrderedDict

# after one newline import 3rd party modules
import unicodecsv  # import whole module
import requests  # import whole module
from bs4 import BeautifulSoup  # import only things that we need

# after another newline import modules that we own
# from naszmodul import costam

# constants should be UPPERCASED and at the begginning of the app
URL = "http://www.bankier.pl/fundusze/notowania/wszystkie"  # we can use both: single ' and double quotes "
HEADERS = (  # this is a tuple, created as a literal
    u'Nazwa funduszu',  # see the u before the string? These can hold ąęćżł
    u'Kurs',
    u'Waluta',
    u'St. zw. 1D',
    u'St. zw. 7D',
    u'St. zw. 1M',
    u'St. zw. 3M',
    u'St. zw. 1R',
    u'St. zw. 3L',
    u'Data',
    u'Ranking 12M',
)

# Pobieramy stronę z internetu
html_doc = requests.get(URL)  # a simple HTTP GET request will be used
html_doc.encoding = 'utf-8'  # but the requests module incorrectly guesses the encoding here
# print html_doc.text # that's the decoded content of the response

# Przeparsujemy treść strony
soup = BeautifulSoup(html_doc.text, 'html.parser')  # parse the contents as a HTML

# mozna tez data = []
# ale konwencja sugeruje tego nie robic jesli lista ma byc pusta
data = list()

# Wybieramy interesujące informacje z tabeli notowań
# look for tables with specified class. Take the first one (0-based indices).
tabela = soup.find_all('table', class_="sortTableMixedData")[0]
for wiersz in tabela.find_all('tr'): # take the data from one row at a time
    tmp_dict = OrderedDict() # we will extract the row data into this dictionary
    # tmp_dict = {
    #    "stopa 1M": '1,23%',
    #    "stopa 3M": '5,00%',
    #    ...
    # }
    komorki = wiersz.find_all('td', recursive=False) # recursive=False means: don't look for nested td's
    # zip(['a','b','c'], [666, 'X', -13]) ==  [('a',666), ('b','X'), ('c',-13)]
    for naglowek, komorka in zip(HEADERS, komorki): # -> ("stopa 1M", '1,23%'), ...
        tmp_dict[naglowek] = komorka.text.strip() # "    \n costam \n \t " -> "costam"
    data.append(tmp_dict)  # add just processed row to our resulting list

# Wypisujemy te informacje do pliku csv
# wypisz nazwy kolumn
plik = open('wynik.csv', 'wb')

# that's the guy that knows how to translate python objects to csv files
writer = unicodecsv.writer(plik, encoding='utf-8')
writer.writerow(HEADERS)  # the headers have to be written manually

for wiersz in data:  # take each computed row
    writer.writerow(wiersz.values()) # {'a': 5, 13: 'lol'}.values() == (5, 'lol')

plik.close()  # we have to close the file handler to make sure that the write buffer is flushed
