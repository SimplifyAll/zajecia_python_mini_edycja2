#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os  # wbudowana biblioteka pythona
import sys

# oddzielone od poprzedniego importu, bo to nie wbudowana czesc pythona
from PIL import (  # importujemy tylko to, bo nie chcemy pisac PIL.Image
    Image,
    ImageStat
)

import io
import exifread #Do wyciągania danych z obrazka

PICTURES_DIR = os.path.dirname(os.path.realpath(__file__))

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
        self.data = exifread.process_file(open(image_path, 'rb'), details=False)

#Myslałem również nad zaimplementowaniem funkcji, ale jednak wygodniej wyciągac dane z obrazka juz w konstruktorze

		# def get_EXIF_data(self, path):
			# data = open(path, 'rb')
	    	# tags = exifread.process_file(data, details=False)
	   	# datad=dict()
	   	# for tag in tags.keys():
			# datad[tag]=tags[tag]
		# return datad

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
        if (
            image.brightness() >= self.min_brightness and
            image.brightness() <= self.max_brightness
        ):
            self.image_list.append(image)
            return True
        return False

    def __repr__(self):  # to pokaze ladne napisy jak zrobimy `print kategorie`
        return "<BrightnessCategory {} with {} images>".format(
            self.name, len(self.image_list))

#Ilość kategorii zależna od argumentu podanego w terminalu
if (len(sys.argv) == 1):
	kategorie = (
	    BrightnessCategory("Ciemne", 0, 90),
	    BrightnessCategory("Srednie", 91, 180),
	    BrightnessCategory("Jasne", 181, 255),
	)
elif (len(sys.argv) == 2):
	ilosc = sys.argv[1]
	kategorie=list();
	ilosc = int(ilosc)
	przedzial=255/ilosc
	for n in xrange(ilosc):
		kategorie.append(BrightnessCategory("Kategoria "+str(n+1), przedzial*n, przedzial*(n+1)))
else:
	print "Nieprawidłowa ilosc argumentow!"
	sys.exit(0)

#Wybor folderu z którego będziemy pobierać obrazki
print '''
Wybierz folder z listy z jakiego chcesz pobrac obrazki:
'''
for x in os.walk(".").next()[1]:
	print x
print "" 
while True:
	a = raw_input()
	if (a==""):
		continue
	else:
		break


for sciezka_obrazka in find_images(PICTURES_DIR+"/"+a):
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
    <body>
        <h1>Galeria obrazkow i zdjec</h1>
        <div>{}</div>
    </body>
</html>
"""

category_template = u"""
<h2>{}</h2>
<div>{}</div>
"""

#Stworzony pop-up niestety nie udalo mi sie do niego zaimplementowac danych (cos z kodowaniem)
image_template = u"""
<span class="dropt" title="TUTAJ POWINNY ZNAJDOWAC SIE DANE OBRAZU">
  <span style="width:500px;"><img style="width: 150px;", src="{}"></span>
</span>
"""

categories_html = ""
for category in kategorie:
    images_html = ""
    for image in category.image_list:
        images_html = images_html + image_template.format(image.image_path) #tutaj również powininen być image.data - niestety cos z kodowaniem

    categories_html = categories_html + category_template.format(category.name, images_html)
    

plikHTML = io.open('galeria.html', 'w', encoding='utf-8')
plikHTML.write(body_template.format(categories_html))
plikHTML.close()

