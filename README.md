# Suspicious History Detektor

Ez a python script egy adott lista domainjeit megnézi a felhasználó összes böngészőjében.

Ha talál egyetlen egy domaint is a listáról, bezáródik 1-es kóddal

### Használat

Nyisd meg a `detector.py` fájlt és hagyd futni ameddig talál valamit.

Szerkezd meg a `domains.json` fájlt, hogy hozzáadj más domaineket is.

Minnél több a domain a `domains.json` fájlban annál tovább tart a keresés, ha a felhasználó régen nyitotta meg bármelyik oldalt.

### Támogatott böngészők
* Chromium
* Chrome
* Edge
* Opera
* OperaGX
* Brave
* Vivaldi
* Firefox
* LibreWolf
* Safari
