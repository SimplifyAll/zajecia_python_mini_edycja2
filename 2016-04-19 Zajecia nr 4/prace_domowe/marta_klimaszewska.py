#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Marta Klimaszewska

import os
import sys

from PIL import (
	Image,
	ImageStat,
)

reload(sys)
sys.setdefaultencoding("utf-8")

def set_parameters():
	#jeżeli mamy argument w konsoli to go bierzemy, a jak nie to dflt value
	if len(sys.argv)>1:
		n = int(sys.argv[1])
	else:
		n = (int)(raw_input("Na ile kategorii jasności chcesz podzielić obrazki?"))

	if len(sys.argv) > 2:
		pictures_dir = str(sys.argv[2])
	else:
		dflt_dir = "/home/marta/Desktop/mini/zajecia_4/pictures"
		user_ans = (str)(raw_input("Czy chcesz użyć domyślnego folderu {}. (t/n)".format(dflt_dir)))
		if user_ans == 't' or user_ans == 'y':
			pictures_dir =dflt_dir
		else:
			pictures_dir = (str)(raw_input("Podaj ścieżkę do folderu z obrazkami"))
	return [n, pictures_dir]

def find_images(start_folder):
	
	for directory, subdirs, files in os.walk(start_folder):
		for name in files:
			yield os.path.join(directory, name)
	

def create_categories(n): 
	kategorie = []
	step = 255/n
	for nr_kategorii in range(1,n+1):
		#teoretycznie niektóre obrazki mogłyby wpadać do dwóch kategorii ale dzięki "break" przy przydzielaniu kategorii - nie będą
		kategorie.append(BrightnessCategory('Kategoria {}'.format(nr_kategorii),step*(nr_kategorii-1), step*nr_kategorii))
	return kategorie

def set_brightness():
	[n, pic_path] = set_parameters()
	kategorie = create_categories(n)
	for sciezka_obrazka in find_images(pic_path):
		obrazek = SuperObrazek(sciezka_obrazka)
		for kategoria in kategorie:
			if kategoria.add_if_brightness_in_range(obrazek):
				break
	return kategorie

def create_cat_html(body_template, kategorie):
	#trzeba było dodać kodowanie w pliku html żeby działało

	category_template = u"""
		<h2>{}</h2>
			<div>{}</div>
	"""

	image_template = u"""
	<a href="{}"><img height = 64 width = 64 src = "{}"></a>
	"""
	categories_html = ""

	for category in kategorie:
		images_html = ""
		for image in category.image_list:
			images_html = images_html + image_template.format(image.image_path,image.image_path)
		categories_html = categories_html + category_template.format(
			category.name, images_html)
	return categories_html


#wczytać wszystkie obrazki

class SuperObrazek(object):

	def __init__(self, image_path):
		self.image_path = image_path
		self.image_object = Image.open(self.image_path)
		self.image_object = self.image_object.convert('RGB')
		self.jasnosc = -1
	
	def __repr__(self):
		return "<SuperObrazek {}>".format(self.image_path)

	def brightness(self):
		if self.jasnosc == -1:
			statystyki = ImageStat.Stat(self.image_object)
			srednie = statystyki.mean
			wyliczona_jasnosc = (
				0.2126 * srednie[0]
				+ 0.7152 * srednie[1]
				+ 0.0722 * srednie[2]
			)
			self.jasnosc = wyliczona_jasnosc
		else:
			wyliczona_jasnosc = self.jasnosc
		return int(wyliczona_jasnosc)


#przetworzyć obrazki - wyliczyć jasność
#kategoryzować obrazki wg jasności

class BrightnessCategory(object):

	def __init__(self, name, min_brightness, max_brightness):
		self.name = name
		self.min_brightness = min_brightness
		self.max_brightness = max_brightness
		self.image_list = []

	def __repr__(self):
		return "<BrightnessCategory {} with {} images".format(
			self.name, len(self.image_list)
		)

	def add_if_brightness_in_range(self, image):
		if (
			image.brightness() >= self.min_brightness and 
			image.brightness() <= self.max_brightness
		):
			self.image_list.append(image)
			return True
		else:
			return False


kategorie = set_brightness()		

#generować galerię w HTML-u

body_template = u"""<html>
	<head>
		<meta charset="utf-8" />
	</head>
	<body>
		<h1>Galeria obrazków i zdjęć</h1>
		<div>{}</div>
	</body>
</html>
"""

categories_html = create_cat_html(body_template, kategorie)

#print body_template.format(categories_html)

Html_file= open("galeria.html","w")
Html_file.write(body_template.format(categories_html))
Html_file.close()