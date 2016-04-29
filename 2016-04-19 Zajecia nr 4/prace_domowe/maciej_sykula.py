#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################
# ./gallery.py plik.html sciezka_obrazkow ilosc_kategorii
#########################################################

import sys
import os  # wbudowana biblioteka pythona
import time

# oddzielone od poprzedniego importu, bo to nie wbudowana czesc pythona
from PIL import (  # importujemy tylko to, bo nie chcemy pisac PIL.Image
    Image,
    ImageStat,
)
from PIL.ExifTags import TAGS

if __name__ == '__main__': #jeśli uruchomiony jest skrypt z konsoli to uruchomi funkcję, a jeśli importujemy to nie
    location = sys.argv[1] #ściąga wszystko co dostanie w cmd od pierwszego do ostatniego elementu
    file_directory = sys.argv[2]
    liczba_kategorii = int(sys.argv[3])


PICTURES_DIR = file_directory


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
            temp = name.split('.')
            image_format = temp[len(temp)-1]
            if image_format in ('gif', 'png', 'jpg', 'jpeg', 'tiff', 'bmp'):
                # print temp[len(temp)-1]
                ret_list.append(os.path.join(directory, name))
    return ret_list

def createThumbnail(image_path, img_file, size = (128, 128)):
    # im = Image.open(file_name)
    im = img_file
    im.thumbnail(size)
    im.save(image_path + ".thumbnail", "JPEG")

class SuperObrazek(object):

    def __init__(self, image_path):
        self.image_path = image_path
        self.image_name = os.path.split(self.image_path)[1]
        self.image_object = Image.open(self.image_path)
        # obrazki moga byc w innych modelach, jak np. CMYK
        self.image_object = self.image_object.convert('RGB')

        img = self.image_object
        # exif_data = img._getexif()
        createThumbnail(self.image_path, img)

    def __repr__(self):  # zeby ladnie mozna zrobic `print image_list`
        return "<SuperObrazek {}, {}>".format(self.image_path, self.image_name)

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
            # print image
            return True
        return False

    def __repr__(self):  # to pokaze ladne napisy jak zrobimy `print kategorie`
        return "<BrightnessCategory {} with {} images>".format(
            self.name, len(self.image_list))

kategorie = list()
start_loop = 0;
tick = 255/liczba_kategorii
end_loop = tick

for i in xrange(0, liczba_kategorii):
    kategorie.append(BrightnessCategory(u"kategoria" + str(i) + ': ' + str(start_loop) +
                                        ' - ' + str(end_loop), start_loop, end_loop))
    start_loop = end_loop + 1
    end_loop = end_loop + tick

files_names = list()
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
    <meta charset="UTF-8">
    </head>
    <body>
        <h1>Galeria obrazków i zdjęć</h1>
        <div style='width:100%'>{}</div>
    </body>
</html>
"""

category_template = u"""
<h2>{}</h2>
<div>{}</div>
"""

image_template = u"""
<img src="{}" style="width: 150px;"/>
<a href='{}'>{}</a>
"""


# obrazek1 = szablon_obrazka.format(sciezka_do_obrazka)
# kategoria1 = szablon_kategorii.format(nazwa, obrazek1 + obrazek2 + ...)
# cala strona = szablon_body.format(kategoria1 + kategoria2 + kategoria3 + ...)

categories_html = u""
for category in kategorie:
    images_html = u""
    for image in category.image_list:
        # path = 'file://' + image.image_path
        path = image.image_path
        images_html = images_html + image_template.format(image.image_path + '.thumbnail', image.image_path, image.image_name)
    categories_html = categories_html + category_template.format(
        category.name, images_html
    )

def saveFile(location='plik.html'):
    f = open(location,'w')
    f.write(body_template.format(categories_html).encode('utf-8'))
    f.close()


saveFile(location)
