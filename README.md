# Chess-Y2K
A python simulation on how much one's ranking can improve on chess.com, 
throughout 90 days of learning.


# Temat
Jaki ranking można osiągnąć na chess.com w 90 dni, na przestrzeni 90 dni nauki?


## Lista etapów i ilość kanałów 
1. Startowy poziom rankingowy - 3 kanały
2. Dzienna ilość zagranych meczów - 3 kanały
3. Procent dokładności na mecz 
4. Dzienna ilość wykonanych puzzli - 3 kanały
5. Dzienny procent zanalizowanych przegranych gier - 3 kanały
6. Dzienna ilość minut materiałów wideo obejrzanych nt. nauki gry w szachy - 3 kanały
7. Dzienna ilość przespanych godzin - 3 kanały
8. Wiek gracza - 4 kanały


## Modyfikatory i ich działanie
Modyfikatory to etapy wpływające na procent dokładności gracza podczas meczy zagranych jednego dnia.
Są nimi etapy: 4., 5., 6., 7. i 8.

Działanie polega na zwiększeniu dolnej wartości przedziału, z którego losowana jest dokładność gracza 
w metodzie eliminacji, oznaczoną jako base. 
Raz dziennie, dla każdego z modyfikatorów, wykonywane jest losowanie z przedziałów o bonusie niskim, średnim, bądź wysokim. 
Ponadto, dla etapu 7. określającego ilość przespanych godzin, możliwe jest wylosowanie wartości ujemnej. Prawdopodobieństwo wylosowania  jest odpowiadająca mu wartość mod. Suma wszystkich modyfikatorów wyznacza wartość
o jaką podn

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

### Symulacja Monte Carlo
- Fancy way of saying "losowanie liczb" 

### Metody modelowania rozkładów
- Fit w Root'cie
- Rozkład Chi kwadrat
