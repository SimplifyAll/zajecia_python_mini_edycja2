#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Pies(object):

    def __init__(self, imie):
        # nazwa atrybutu nie musi sie zgadzac z nazwa argumentu
        self.moje_imie = imie
        # dobra praktyka: najlepiej sie odwolywac juz nie do imie, ale do
        # self.moje_imie bo byc moze np. imie jest zmieniane wyzej na UPPERCASE
        print "Pies {} wchodzi do gry!".format(self.moje_imie)

    def przedstaw_sie(self):
        print "Nazywam sie {}".format(self.moje_imie)

    def __repr__(self):  # funkcja __repr__ musi zwracac napis, a nie printowac
        return "<Obiekt psa o imieniu {}>".format(self.moje_imie)


lista_psow = []

lista_psow.append(Pies("reksio"))
lista_psow.append(Pies("hauhau"))

lista_psow[0].przedstaw_sie()

print lista_psow
