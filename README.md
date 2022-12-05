# Chess-Y2K
A python simulation on how much time it takes for one to reach 2000 ranking points on chess.com, 
having played at least a game daily.

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


# Temat
Ile czasu potrzeba, żeby osiągnąć 2000 punktów rankingowych na chess.com, 
grając przynajmniej jedną grę dziennie?


## Lista etapów
1. Startowy poziom rankingowy
2. Dzienna ilość zagranych meczów
3. Dzienna delta punktów rankingowych 
4. Średni dzienny procent dokładności na mecz 
5. Dzienna ilość wykonanych puzzli 
6. Dzienna ilość wykonanych analiz przegranych gier 
7. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy 
8. Dzienna ilość przespanych godzin 
9. Wiek gracza 


# Etapy
## 1. Startowy poziom rankingowy
- Rozkład dyskretny
- Dużo czasu: 100-899
- Średnio czasu: 900-1399
- Średnio mało czasu: 1399-1999

## 2. Dzienna ilość zagranych meczów
- Rozkład dyskretny
- Dużo czasu: 1-3 
- Średnio czasu: 4-8 
- Mało czasu: 9-25 

## 3. Dzienna delta punktów rankingowych
- Rozkład dyskretny 
- Zależny od dziennej ilości zagranych meczów 
- Dużo czasu: -175 - +10 
- Średnio czasu: +10 - +30 
- Mało czasu: +30 - +200 

## 4. Średni dzienny procent dokładności na mecz 
- Rozkład zmiennej ciągłej 
- Dużo czasu: 0%-70% 
- Średnio czasu: 70%-85% 
- Mało czasu: 85%-100% 

## 5. Dzienna ilość wykonanych puzzli 
- Rozkład dyskretny 
- Dużo czasu: 0-3 
- Średnio czasu: 3-10 
- Mało czasu: 10-30 

## 6. Średni dzienny procent zanalizowanych przegranych gier 
- Rozkład dyskretny 
- Dużo czasu: 0%-25%
- Średnio czasu: 25%-70%
- Mało czasu: 70%-100%

## 7. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy 
- Rozkład zmiennej ciągłej 
- Dużo czasu: 0-10
- Średnio czasu: 10-20
- Mało czasu: 20-60

## 8. Dzienna ilość przespanych godzin 
- Rozkład zmiennej ciągłej 
- Dużo czasu: 0h-5h
- Średnio czasu: 5h-7h
- Mało czasu: 7h-10h

## 9. Wiek gracza 
- Rozkład dyskretny 
- Wyznacza peak intelektualny, związany z możliwością przyswajania nowych informacji 
- Dużo czasu: 0-10 AND 35+
- Średnio czasu: 28-35
- Mało czasu: 10-28

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
- Zmienna losowa przyjmuje nieskończoną liczbę różnych wartości, np. wartości z przedziału <2, 7> 

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
