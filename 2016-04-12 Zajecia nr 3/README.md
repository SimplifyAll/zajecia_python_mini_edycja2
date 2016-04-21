# Zajęcia 3

Adres serwisu API z którego korzystamy: http://fixer.io/

## Uwaga do zajęć
Bardzo przepraszam za zamieszanie jakie powstało w kodzie podczas zajęć.
Przygotowałem działające rozwiązanie (do którego ostatecznie doszliśmy),
niestety w trakcie wspólnego pisania zbyt mocno zaufałem intuicji zamiast
sprawdzić jakiego formatu danych będziemy potrzebować do wyrysowania wykresu
funkcją `plt`.

Wartości dydaktyczne z tego są następujące:

+ nie zawsze pisanie "przyrostowe" jest najlepszym podejściem (czytaj: podejścia
  MVP czy TDD nie zawsze są najlepszym rozwiązaniem)
+ zawsze zanim się napisze fragment wczytujący dane do jakiejś struktury, trzeba
  sprawdzić jaki format danych będzie mógł być dalej użyty (w naszym przypadku
  w funkcji `plt`)
+ nie zawsze pisanie kodu wygląda tak, że od razu wiemy co i jak zrobić. Czasami
  trzeba napisany kod kilkukrotnie zmienić, aby dopasować go do nieprzewidzianych
  wcześniej okoliczności.

Tymczasem ja obiecuję, że w przyszłości podobne sytuacje nie będą miały miejsca.

## Praca domowa z 3 zajęć

Na rozwiązania tym razem jest niestety mniej czasu, ponieważ następne zajęcia
już za tydzień. Dlatego prosimy przesyłać rozwiązania jak zawsze na
event@daftcode.pl do 17 kwietnia (niedziela) włącznie. Termin nieprzekraczalny:
poniedziałek 8 rano, z późniejszymi rozwiązaniami możemy nie wyrobić się ze
sprawdzaniem.

### Zadania najprostsze

- pozwolić na podanie wartości ustawionych dotychczas jako stałe (waluta
  bazowa, waluty docelowe) jako parametrów do funkcji. Podać domyślne rozsądne
  wartości (na przykład takie jak dotychczas były zapisane jako stałe)
- poprawić zapisywane daty kursów - zamiast takich jakie wynikają ze zmiennej
  `curr_date`, takie jakie są zwracane przez usługę internetową.
  Hint: sparsować napis z datą (`strptime`, podając właściwy `format`).

### Zadania proste

- zmodyfikować kod tak, aby struktura słownika nie była definiowana w trakcie
  jego uzupełniania, ale przed tym. Hint: `DefaultDict`. Ma to na celu
  zwiększenie czytelności kodu i jego łatwiejsze utrzymanie (modyfikowanie) w
  przyszłości.
- zmienić słownik na napisaną przez siebie klasę, która pozwala na proste użycie
  w pyplocie (czyli nie znacząco trudniej niż teraz). Cel: optymalizacja i/lub
  zwiększenie czytelności kodu. Hint: sprawdzić dokumentację `pyplot.plt`.

### Zadania umiarkowanie proste

- przybliżyć wykresy funkcjami liniowymi (liniami trendu), narysować je i
  przewidzieć wynik na kilka interwałów do przodu (liczba interwałów podana jako
  parametr). Przykładowo 3 interwały ponad ostatnią znaną wartość.
- to samo co powyżej, ale przybliżenie funkcją wielomianową 3 stopnia (albo
  stopnia ustawialnego przez parametr)

### Zadania proste z gwiazdką

- dodać własną wymyśloną funkcjonalność (na przykład wykorzystanie innych
  funkcji używanego przez nas API) lub poprawki w kodzie wedle własnego uznania.
  To zadanie wymaga koniecznie co najmniej jednego zdania komentarza co się
  zmieniło :)

## Omówienie pracy domowej z drugich zajęć
Wojtek okomentował wszystkie nadesłane rozwiązania.

Plik z rozwiązaniami możecie pobrać tu: [rozwiazania_pracy_domowej_3.zip](https://github.com/daftcode/zajecia_python_mini_edycja2/raw/master/2016-04-12%20Zajecia%20nr%203/rozwiazania_pracy_domowej_3.zip)

## Wymagania
Do zadania na zajęciach 3 będą nam potrzebne biblioteki:

`requests` (instalowaliśmy na poprzednich zajęciach) oraz `matplotlib`.
```
sudo pip install matplotlib
```
lub
```
sudo apt-get install python-matplotlib
```

### Mac OS X

Osoby pracujące na komputerach ze zgniłym jabłkiem mogą napotkać na problem przy
importowaniu matplotliba (w pythonie). Rozwiązanie problemu jest 2-linijkowe,
można je znaleźć tutaj:
https://coderwall.com/p/-k_93g/mac-os-x-valueerror-unknown-locale-utf-8-in-python
