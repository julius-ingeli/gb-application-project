# gb-application-project


Toto slúži ako riešenie 2. časti otázok zaslaných

Program je napísaný v pythone, využíva knižnice requests, json a datetime.

Pomocou requestu z API by sa mali dáta získať, prehodiť do .json formátu

V Pythone nie je najlepší natívny spôsob ako zaručiť to aby sa natívne v daný čas vždy tento skript spustil, avšak na platforme Linux to ide pomocou funckie crontab, kde sa iba zadá do crontab súboru nasledovné:

```
0 7 * * * /usr/bin/python3 ~/extractor.py
```

Alternatívne, na Windowse pomocou Task Scheduleru.



## Poznámka

Počas vývoju tohoto projektu API na golemio nešlo, hádzalo 501 error, takže nedá sa úplne overiť či toto je funkčný produkt.