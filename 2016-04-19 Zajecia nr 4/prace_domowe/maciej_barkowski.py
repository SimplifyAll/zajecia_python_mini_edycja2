#!/usr/bin/env python
#-*-coding: utf-8-*-
# plik obrazki1.py

# Aby zawarto¶æ pliku html by³a prwid³owo wy¶wietlana 
# w przegl±darce ustawi³em w IDE kodowanie ISO-8859-2

import os, sys, argparse

from PIL import (
	Image,
	ImageStat,
	ExifTags,
)

class SuperObrazek(object):
	
	def __init__(self, imagePath):
		self.imagePath = imagePath
		self.imageObject = Image.open(self.imagePath)
		self.imageObject = self.imageObject.convert("RGB")
		self.jasnosc = list()

	def thumbnails(self):
		thumb = os.path.splitext(self.imagePath)[0] + ".thumbnail"
		try:
			im = Image.open(self.imagePath)
			im.thumbnail((128, 128), Image.ANTIALIAS)
			im.save(thumb, "gif")
		except IOError:
			print "Brak mo¿liwo¶ci stworzenia miniaturki z pliku %s" % self.imagePath
		return thumb

	def brightness(self):
		if len(self.jasnosc) != 0:
			return int(self.jasnosc[-1])
		else:
			statystyki = ImageStat.Stat(self.imageObject)  # ¶rednia z jasno¶ci wszystkich pikseli
			srednie = statystyki.mean # ¶rednie jasno¶ci pikseli
			wyliczonaJasnosc = (
				0.2126 * srednie[0]
				+ 0.7152 * srednie[1]
				+ 0.0722 * srednie[2]
			)
			self.jasnosc.append(wyliczonaJasnosc)
			return int(wyliczonaJasnosc) # konwersja na int aby jasno¶æ nie by³a float
	
	def __repr__(self):
		return "<SuperObrazek> {}".format(self.imagePath)
	

class BrightnessCategory(object):
	
	def __init__(self, name, minBrightness, maxBrightness):
		self.name = name
		self.minBrightness = minBrightness
		self.maxBrightness = maxBrightness
		self.imageList = list()
	
	def addIfBrightnessInRange(self, image):
		jasnosc = image.brightness()
		if jasnosc >= self.minBrightness and jasnosc <= self.maxBrightness:
			self.imageList.append(image)
			return True
		return False
	
	def __repr__(self):
		return"<BrightnessCategory {} with {} images>".format(
				self.name, len(self.imageList))

	########
	#*MAIN*#
	########

if __name__ == "__main__":
	
	def findImages(startFolder):
		retList = list()
		for directory, subdirs,  files in os.walk(startFolder):
			for name in files:
				if os.path.splitext(name)[-1].lower() != ".jpg": # dopisujemy do retList tylko pliki *.jpg z wybranego katalogu
					continue
				retList.append(os.path.join(directory,name)) 
		return retList # zwraca listê w postaci /¶cie¿ka_do_pliku/plik
		
	def html(kategorie, plik):
		bodyTemplate = """
		<html>
			<body>
				<h1>Galeria obrazów i zdjêæ</h1>
				<div>{}</div>
			</body>
		</html>
		"""
		categoryTemplate = """
		<h2>{}</h2>
		<div>{}</div>
		"""
		imageTemplate = """
		<p>
			{}
			<a href="{}">
				<img src="{}" alt="Link do obrazu" style="width: 150px;">
			</a>
		</p>
		"""
		
		categoriesHtml = ""
		for kategoria in kategorie:
			imagesHtml = ""
			for image in kategoria.imageList:
				name = os.path.split(image.imagePath)
				imagesHtml = imagesHtml + imageTemplate.format(name[1], image.imagePath, image.thumbnails())
			categoriesHtml = categoriesHtml + categoryTemplate.format(kategoria.name, imagesHtml)
		
		htmlFile = open("%s.html" % plik, "w")
		htmlFile.write(bodyTemplate.format(categoriesHtml))
		htmlFile.close()
		
	parser = argparse.ArgumentParser("Pomoc do programu obrazki1")
	parser.add_argument("string", type = str, nargs = 2, help = "pierwszy argument - katalog docelowy, drugi - nazwa pliku html")
	parser.parse_args()
		
	PICTURES_DIR = sys.argv[1]  # katalog z obrazkami tylko jako argument
	htmlFile = sys.argv[2]  # plik docelowy tylko jako argument
	
	kategorie = (
		BrightnessCategory("Jasno¶æ w zakresie %s - %s" % (0, 90), 0, 90),  # ciemne
		BrightnessCategory("Jasno¶æ w zakresie %s - %s" % (91, 180), 91, 180),  # ¶rednie
		BrightnessCategory("Jasno¶æ w zakresie %s - %s" % (181, 255), 181, 255),  # jasne
	)
		
	for sciezka in findImages(PICTURES_DIR):
		obrazek = SuperObrazek(sciezka)
		for kategoria in kategorie:
				
			if kategoria.addIfBrightnessInRange(obrazek):
				break
	html(kategorie, htmlFile)
							
