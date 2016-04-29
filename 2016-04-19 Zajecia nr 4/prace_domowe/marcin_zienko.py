#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os  # wbudowana biblioteka pythona
import sys

# oddzielone od poprzedniego importu, bo to nie wbudowana czesc pythona
from PIL import (  # importujemy tylko to, bo nie chcemy pisac PIL.Image
    Image,
    ImageStat,
)


PICTURES_DIR = "/home/marcin/projects/daftcode/lab4/pictures"


# funkcja find_images nam da cos takiego:
# [
# '/home/mini/zajecia/lab4/pictures/5.jpg',
# '/home/mini/zajecia/lab4/pictures/subway/tunnel/1.jpg',
# '/home/mini/zajecia/lab4/pictures/subway/tunnel/2.jpg'
# ]

def find_images(start_folder):
    ret_list = list()
    # uwaga: nie wykorzystamy zmiennej subdirs, to nie znaczy, ze nie powinna
    # byc odpowiednio nazwana
    for directory, subdirs, files in os.walk(start_folder):
        for name in files:
            ret_list.append(os.path.join(directory, name))
    return ret_list


class SuperObrazek(object):

    def __init__(self, image_path):
        self.image_path = image_path
        self.image_object = Image.open(self.image_path)
        # obrazki moga byc w innych modelach, jak np. CMYK
        self.image_object = self.image_object.convert('RGB')

    def __repr__(self):  # zeby ladnie mozna zrobic `print image_list`
        return "<SuperObrazek {}>".format(self.image_path)

    def brightness(self):
        statystyki = ImageStat.Stat(self.image_object)
        srednie = statystyki.mean
        wyliczona_jasnosc = (  # naprawde to relative luminance, warto poczytac
            0.2126 * srednie[0]  # en.wikipedia.org/wiki/Relative_luminance
            + 0.7152 * srednie[1]
            + 0.0722 * srednie[2]
        )

        return int(wyliczona_jasnosc)


class BrightnessCategory(object):

    def __init__(self, name, min_brightness, max_brightness):
        self.name = name  # przypiszmy sobie do naszego obiektu atrybuty
        self.min_brightness = min_brightness  # nazwy nie musza byc takie same
        self.max_brightness = max_brightness  # ale po co wymyslac kolejne?
        # jak widac konstruktor moze robic tez inne rzeczy niz
        # przypisania argumentow
        self.image_list = list()

    def add_if_brightness_in_range(self, image):  # zwraca czy dodal
        jasnosc = image.brightness()
        if (
            jasnosc >= self.min_brightness and
            jasnosc <= self.max_brightness
        ):
            self.image_list.append(image)
            return True
        return False

    def __repr__(self):  # to pokaze ladne napisy jak zrobimy `print kategorie`
        return "<BrightnessCategory {} with {} images>".format(
            self.name, len(self.image_list))


ile = int(sys.argv[1])
kategorie = list()
start = 0
podzial = int(255/ile)
koniec = podzial
x = 0
for k in range(ile):
    x = x + 1
    k = BrightnessCategory(u"Kategoria jasności {}".format(x), start, koniec)
    start = koniec + 1
    koniec = koniec + podzial
    kategorie.append(k)
kategorie.max_brightness[len(kategorie-1)] = 255


#kategorie = (
#    BrightnessCategory("Ciemne", 0, 90),
#    BrightnessCategory(u"Średnie", 91, 180),
#    BrightnessCategory("Jasne", 181, 255),
#)


for sciezka_obrazka in find_images(PICTURES_DIR):
    obrazek = SuperObrazek(sciezka_obrazka)
    for kategoria in kategorie:
        # ponizsza linijka sprobuje dodac do kolejnych kategorii i nam zwroci
        # za kazdym razem True/False czy sie udalo - wykorzystamy to jako
        # sprawdzany warunek instrukcji if
        if kategoria.add_if_brightness_in_range(obrazek):
            break  # nie sprawdzamy kolejnych kategorii dla oszczednosci czasu
        # else:
        #   continue


body_template = u"""<html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    </head>

    <body>
        <h1>Galeria obrazków i zdjeć</h1>
        <div>{}</div>
    </body>
</html>
"""

category_template = u"""
<h2>{}</h2>
<div>{}</div>
"""

image_template = u"""
<img src="{}" style="width: 150px;"/>
"""

# obrazek1 = szablon_obrazka.format(sciezka_do_obrazka)
# kategoria1 = szablon_kategorii.format(nazwa, obrazek1 + obrazek2 + ...)
# cala strona = szablon_body.format(kategoria1 + kategoria2 + kategoria3 + ...)

categories_html = ""
for category in kategorie:
    images_html = ""
    for image in category.image_list:
        images_html = images_html + image_template.format(image.image_path)
    categories_html = categories_html + category_template.format(
        category.name, images_html
    )
kod_html = body_template.format(categories_html).encode('utf-8')
kod = open('galeria.html', 'w')
kod.write(kod_html)
