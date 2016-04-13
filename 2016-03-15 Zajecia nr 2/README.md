# Zajęcia 2

## Praca domowa z drugich zajęć
Poprawić kod programu napisanego na zajęciach w ten sposób, aby:

- był bardziej optymalny pod względem obliczeniowym jak i pamięciowym
- miał większą liczbę "sprytnych" funkcji, czyli takich, które pozwalają
  zmniejszyć ilość napisanego kodu, a dają ten sam efekt końcowy. Hint:
  dokumentacja BeautifulSoup, dokumentacja Pythona (built-in functions)
- eliminował problem pustych linii, które są generowane przez obecny program
- wpisywał do wyniku rating (ostatnia kolumna ze źródłowej tabeli), który póki
  co jest pusty lub jest znakiem "-". Rzecz jasna w formie tekstowej, nie
  obrazkowej.

## Rozwiązania pracy domowej z drugich zajęć
Czekamy na nadsyłanie rozwiązań na event@daftcode.com do 10 kwietnia (niedziela)
włącznie :) Najciekawsze rozwiązania omówimy na zajęciach!

## Omówienie pracy domowej z drugich zajęć
Wojtek przygotował super-skrypt który porównuje wszystkie nadesłane rozwiązania.

Możecie go pobrać tu: rozwiazania_prac_domowych.zip

Odpalanie: `python check_app.py`

Wyjście z tego skryptu jest następujące:

```
av: 0.21 s, top: 0.17 s - valid - 0.0000% - puchalski_pawel - +lxml, +oneliner, +Najszybszy wynik!, -absoutnie nieczytelna dla nooba
av: 0.63 s, top: 0.62 s - valid - 0.0000% - webster58 - REFFERENCE
av: 0.66 s, top: 0.65 s - valid - 0.0000% - cudzilo_tomasz - +lxml, +parse_only, +podzial logiki na funkcje, +imap,ifilter, -list(imap(...))
av: 0.80 s, top: 0.79 s - valid - 0.0000% - okuniewski_marcin - +lxml, +przedzial wyszukiwania, +filtrowanie elementow
av: 0.85 s, top: 0.85 s - invalid - 0.0000% - misiewicz_michal - +lxml, +przeczial wyszukiwania -inne hedery
av: 0.87 s, top: 0.86 s - invalid - 0.0000% - konat_kamil - +podzial na fukncję,  -nieoptymalne, --globals
av: 0.94 s, top: 0.94 s - invalid - 0.0000% - siankiewicz_kamil - 
av: 0.95 s, top: 0.94 s - invalid - 0.0000% - antoniak_jan - -nieoptymalne
av: 0.98 s, top: 0.98 s - invalid - 0.0000% - barkowski_maciej - +podzial na klasy, +wartosci domyslme, +input line params, -nieoptymalne
av: 0.99 s, top: 0.99 s - invalid - 0.0000% - stelmach_dawid - +zakresy wyszukiwania, +headers
av: 1.08 s, top: 1.06 s - invalid - 0.0000% - umanski_mikolaj - +with, +zapis lini w glownej petli, +filrowanie wyszukiwania
av: 1.10 s, top: 1.09 s - invalid - 0.0000% - kochanksa_paula -  -nieoptymalne
av: 1.21 s, top: 1.09 s - invalid - 0.0000% - antek - stan z zajec
av: 1.22 s, top: 1.21 s - invalid - 0.0000% - klimaszewska_marta - -"0" != "-" w ostaniej kolumnie, -nieoptymalne
av: 1.23 s, top: 1.22 s - invalid - 0.0000% - zienko_marcin - -poziom skomplikowania,-nieoptymalne
av: 1.25 s, top: 1.25 s - invalid - 0.0000% - wadolkowski_adam - -nieoptymalne
av: 1.27 s, top: 1.25 s - invalid - 0.0000% - pankowski_marek - +filtrowanie po klasach
av: 1.28 s, top: 1.26 s - invalid - 0.0000% - sykula_maciej - -nieptymalny, - mocno przekombinowane wyciągnie cyfry
av: 14.79 s, top: 14.73 s - invalid - 0.0000% - przywarty_adam -  ... -czas wykonania ....
```
