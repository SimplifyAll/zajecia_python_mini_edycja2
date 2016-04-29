# Zajęcia 5

Prace domowe z poprzednich zajęć wraz z komentarzami są w katalogu zajęć 4.

## Wymagania

Będzie nam potrzebny pakiet `bottle`.
Aby go zainstalować, wystarczy wydać w konsoli komendy:

- `sudo pip install bottle` LUB
- `pip install --user bottle`.

## Praca domowa z 5 zajęć

Na przykładzie naszego kodu z zajęć przyjrzymy się jeszcze dokładniej wyjątkom
i context managerom (`with`). Pokażę też jak można zastąpić część z zapytań
zapytaniami AJAXowymi. Niemniej chętni mogą spróbować swoich sił już w pracy
domowej, szczególnie, że jest sporo czasu, bo 2 tygodnie do następnych zajęć.

### Zadania tak łatwe, że aż śmieszne

- nie pokazywać numerów tasków, ale zachować możliwość kasowania oraz toggle
- użyć nie domyślnego sposobu picklowania (protokół 0), tylko najwyższego
  ([dokumentacja](https://docs.python.org/2/library/pickle.html#data-stream-format)).
  Uwaga, pliki trzeba [otwierać w trybie binarnym](https://docs.python.org/2/library/functions.html#open).
- dodać własne [strony błędów 404](http://bottlepy.org/docs/dev/tutorial.html#error-pages) -
  mogą być czystym tekstem, bez dodatkowego szablonu

### Zadania łatwe miłe i przyjemne

- dodać w szablonie HTML style css które poprawią wygląd strony
- dodać w szablonie HTML obiekty typu np. `div`, które ułatwią powyższe ostylowanie

### Zadania łatwe, choć wymagające zerknięcia w dokumentację

- dodać szablon styli w formie osobnego pliku css (trzeba móc
  [serwować statyczne pliki](http://bottlepy.org/docs/dev/tutorial.html#routing-static-files))
- dodać [zapytanie AJAXowe POST](https://api.jquery.com/jquery.post/) w dodawaniu
  nowego zadania do listy. Jako zabezpieczenie pozwalać na dotychczasowe zachowanie
  na wypadek jeśli użytkownik nie ma włączonego javascriptu (hint: kod w pythonie
  musi sprawdzać czy to było zapytanie ajaxowe czy nie i zwracać różne odpowiedzi)
- dodać [zapytanie AJAXowe DELETE](https://api.jquery.com/jquery.ajax/) w usuwaniu
  zadania do listy (hint: tu trzeba będzie dokodzić kolejny endpoint, który będzie
  akceptować zamiast metody GET metodę DELETE).
- dodać możliwość zamiast/oprócz picklowania,
  [serializację do formatu JSON](https://docs.python.org/2/library/json.html#json.dump)
  (i analogicznie deserializację)
- dodać własną wymyśloną funkcjonalność i/lub ulepszenia w kodzie aplikacji


## Lektura dodatkowa

By popular request, przedstawiamy linki, które pomogą przyswoić zawczasu materiał
związany z [wyjątkami (od "What is Exception?")](http://www.tutorialspoint.com/python/python_exceptions.htm)
oraz [context managerami](http://effbot.org/zone/python-with-statement.htm).
Ba, nawet jest link do [dekoratorów](http://www.learnpython.org/en/Decorators).