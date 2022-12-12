# Chess-Y2K
A python simulation on what ranking can one achieve on chess.com, 
having played at least a game daily for a month.

---
## TODO:
- Phase 2. implementation
- Phase 3. implementation
- Phase 4. implementation
- Phase 5. implementation
- Phase 6. implementation
- Phase 7. implementation
- Phase 8. implementation
- Phase 9. implementation
- Consider using a function with a random +/- delta instead of hard coded values for each phase
- Consider simulating the process daily, with a track of ranking points
- Add continuous variable distributions



# Temat
Jaki ranking można osiągnąć na chess.com w 90 dni, grając przynajmniej jedną grę dziennie?


## Lista etapów 
1. Startowy poziom rankingowy 
2. Dzienna ilość zagranych meczów 
3. Średni dzienny procent dokładności na mecz 
4. Dzienna ilość wykonanych puzzli 
5. Dzienny procent zanalizowanych przegranych gier 
6. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy 
7. Dzienna ilość przespanych godzin 
8. Wiek gracza 


## Etapy losowane dziennie
- 2
- 3
- 4
- 5
- 6
- 7
- 8


# Etapy
## 1. Startowy poziom rankingowy
- Rozkład dyskretny
- Wysoki ranking: 100-899
- Średni ranking: 900-1399
- Średnio niski ranking: 1399-1999

## 2. Dzienna ilość zagranych meczów
- Rozkład dyskretny
- Wysoki ranking: 1-2 
- Średni ranking: 3-6 
- Niski ranking: 7-30 

## 3. Średni dzienny procent dokładności na mecz 
- Rozkład zmiennej ciągłej 
- Wysoki ranking: 85%-100%
- Średni ranking: 70%-85% 
- Niski ranking: 1%-70% 

## 4. Dzienna ilość wykonanych puzzli 
- Rozkład dyskretny 
- Wysoki ranking: 0-3 
- Średni ranking: 4-10 
- Niski ranking: 11-30 

## 5. Dzienny procent zanalizowanych przegranych gier 
- Rozkład dyskretny 
- Wysoki ranking: 0%-25%
- Średni ranking: 25%-70%
- Niski ranking: 70%-100%

## 6. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy 
- Rozkład zmiennej ciągłej 
- Wysoki ranking: 20-60
- Średni ranking: 10-20
- Niski ranking: 0-10

# ZMIANA
## 7. Dzienna ilość przespanych godzin 
- Rozkład dyskretny 
- Wysoki ranking: 0h-5h
- Średni ranking: 6h-7h
- Niski ranking: 8h-10h

## 8. Wiek gracza 
- Rozkład dyskretny 
- Wyznacza peak intelektualny, związany z możliwością przyswajania nowych informacji 
- Wysoki ranking: 0-10 AND 35+
- Średni ranking: 28-35
- Niski ranking: 10-28


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
