# Chess-Y2K
A python simulation on how much one's ranking can improve on chess.com, 
having played at least a game daily for a month.


# Temat
Jaki ranking można osiągnąć na chess.com w 90 dni, grając przynajmniej jedną grę dziennie?


## Lista etapów 
1. Startowy poziom rankingowy 
2. Dzienna ilość zagranych meczów 
3. Procent dokładności na mecz 
4. Dzienna ilość wykonanych puzzli 
5. Dzienny procent zanalizowanych przegranych gier 
6. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy 
7. Dzienna ilość przespanych godzin 
8. Wiek gracza


## Działanie dziennych symulacji
Losowana jest delta acc. Zależnie od etapu i przedziału może być duża, średnia, niska, bądź ujemna.

Wiek wpływa na wygrywanie gier:
- Jeśli jesteś młody wygrywasz dużo więcej gier
- Jeśli jesteś średni wygrywasz wiele więcej gier
- Jeśli jesteś stary wygrywasz niewiele więcej gier

A good idea is not to amplify the acc. score directly, but to do so on the probability of generating higher acc.


# Etapy
## 1. Startowy poziom rankingowy
- Rozkład dyskretny
- Wysoki ranking: 100-899
- Średni ranking: 900-1399
- Średnio niski ranking: 1399-1999

## 2. Dzienna ilość zagranych meczów
- Rozkład dyskretny
- Wysoki ranking: 7-30
- Średni ranking: 3-6 
- Niski ranking: 1-2 

## 3. Procent dokładności na mecz 
- Rozkład zmiennej ciągłej 
- Wysoki ranking: 85%-99%
- Średni ranking: 70%-84% 
- Niski ranking: 1%-69% 

## 4. Dzienna ilość wykonanych puzzli 
- Rozkład dyskretny 
- Wysoki ranking: 0-3 
- Średni ranking: 4-10 
- Niski ranking: 11-30 

## 5. Dzienny procent zanalizowanych przegranych gier 
- Rozkład zmiennej ciągłej 
- Wysoki ranking: 70%-100%
- Średni ranking: 25%-69%
- Niski ranking: 0%-24%

## 6. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy 
- Rozkład dyskretny 
- Wysoki ranking: 20-60
- Średni ranking: 10-19
- Niski ranking: 0-9

## 7. Dzienna ilość przespanych godzin 
- Rozkład dyskretny 
- Wysoki ranking: 8h-10h
- Średni ranking: 6h-7h
- Niski ranking: 0h-5h

## 8. Wiek gracza 
- Rozkład dyskretny 
- Wyznacza peak intelektualny, związany z możliwością przyswajania nowych informacji 
- Wysoki ranking: 5-28
- Średni ranking: 29-45
- Niski ranking: 1-4 AND 46-90


## Lista kluczowych pojęć i zagadnień
- Symulacja
- Modelowanie
- Zmienna losowa ciągła
- Zmienna dyskretna
- Generowanie liczb z rozkładu zmiennej ciągłej
- Generowanie liczb z rozkładu zmiennej dyskretnej
- Symulacja Monte Carlo
- Metody dopasowania/modelowania rozkładów

## Podstawowe pojęcia i zagadnienia
### Symulacja
- Wielokrotne generowanie liczb

### Modelowanie
- Badanie rozkładu liczb z symulacji w celu opisania go funkcją matematyczną

### Zmienna losowa ciągła
- Zmienna losowa przyjmująca nieskończoną liczbę różnych wartości, np. wartości z przedziału <2, 7> 

### Zmienna dyskretna
- Zmienna dyskretna to zmienna losowa, która przyjmuje wartości ze skończonego zbioru, np. {2, 1, 3, 7}

### Rozkład prawdopodobieństwa
- Miara wartości prawdopodobieństw przypisanych danym zmiennym losowym
- Zależnie od wartości zmiennych losowych może przyjmować różne kształty, stąd mamy np. rozkład równomierny, rozkład wykładniczy

### Generowanie liczb z rozkładu zmiennej losowej
- Metoda odwróconej dystrybuanty
- Metoda eliminacji

### Generowanie liczb z rozkładu zmiennej dyskretnej
- [Python](https://www.shorturl.at/DMS03)

### Symulacja Monte Carlo
- Fancy way of saying "losowanie liczb" 

### Metody modelowania rozkładów
- [Python](https://www.shorturl.at/aeOU5)
- Fit w Root'cie
- Rozkład Chi kwadrat
