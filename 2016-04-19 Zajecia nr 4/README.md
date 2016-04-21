# Zajęcia 4

## Wymagania

Materiały do zajęć (kilkadziesiąt obrazków) są w pliku [pictures.zip](https://github.com/daftcode/zajecia_python_mini_edycja2/raw/master/2016-04-19%20Zajecia%20nr%204/pictures.zip).

Będzie nam dodatkowo potrzebny pakiet Pillow w wersji 3.0.0.
Aby go zainstalować, wystarczy wydać w konsoli komendy:

- `sudo apt-get install python-dev`
- `sudo apt-get install libjpeg-dev`
- `sudo apt-get install zlib1g-dev`
- `sudo pip install Pillow==3.0.0`.


## Lintery

Część osób już skorzystała przy poprzedniej pracy domowej z pomocy linterów,
czyli programów wskazujących na problemy stylistyczne z kodem (brak spacji,
nieodpowiednie wcięcia itp).

Dla chętnych polecamy wykorzystanie linterów do Sublime'a. Trzeba [zainstalować
obsługę pluginów do Sublime'a](https://packagecontrol.io/installation), a
następnie [doinstalować](https://packagecontrol.io/docs/usage) jakiegoś lintera,
przykładowo [Python Flake​8 Lint](https://packagecontrol.io/packages/Python%20Flake8%20Lint)
czy [Sublime​Linter](https://packagecontrol.io/packages/SublimeLinter) plus 
[Sublime​Linter-pep​8](https://packagecontrol.io/packages/SublimeLinter-pep8) plus
`sudo pip install pep8`.

Warto zauważyć, że różne IDE do Pythona typu PyCharm mają najczęściej wbudowanego
lintera. Co nie znaczy, że Sublime z pluginami sobie radzi z czymkolwiek gorzej.


## Praca domowa

Kod z zajęć został okomentowany, warto poczytać.

Na rozwiązania tym razem jest znowu mniej czasu, ponieważ następne zajęcia
już za tydzień. Dlatego prosimy przesyłać rozwiązania jak zawsze na
event@daftcode.pl do 24 kwietnia (niedziela) włącznie. Termin nieprzekraczalny:
poniedziałek 8 rano, z późniejszymi rozwiązaniami możemy nie wyrobić się ze
sprawdzaniem.

Praca domowa ma tym razem wiele punktów, można wybrać dowolne zadania z poniższych.

- w wygenerowanym dokumencie html
    - dodać nazwy plików które są linkiem
        - JEŚLI w IPTC/EXIF znajdują się: adres email lub url - link do jednego
          napotkanego maila lub urla
        - link do oryginalnego pliku obrazka, jeśli nie jest spełniony poprzedni
          warunek
    - dodać popup lub dymek zawierający wszystkie metadane IPTC/EXIF
- pogrupować program na funkcje wedle własnego uznania
- pozwolić na podanie dowolnej liczby kategorii `n` (z linii poleceń) tak, aby było
  `n` kategorii o kolejnych zakresach spełniających warunek `max-min = 255 / n`
- pozwolić na podanie dowolnego folderu jako tego, który zawiera obrazki
- wypisywać HTML galerii do pliku (nazwa stała lub podana jako argument w konsoli)
  zamiast printować na konsolę
- stworzyć gdzieś w kodzie generator(y) (`yield`) (tam, gdzie ma to sens)
- wygenerować miniaturki (lub wykorzystać istniejące, jeśli są w pliku) i je
  pokazywać zamiast pełnych obrazków (dzięki temu strona się będzie szybciej
  ładować)
- rozwiązać problem z unikodem jeśli są polskie znaki w kodzie (na zajęciach nie
  działało `galeria.py > wynik.html`)
- przerobić funkcję `SuperObrazek.brightness()` tak, aby liczyła jasność tylko raz,
  a przy następnym wywołaniu zwracała poprzednio policzony wynik.
- usprawnić kod wedle własnego uznania - optymalizacje, dobre praktyki itp.
