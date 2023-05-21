'''
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author:  Tereza Sindelarova
email: lycosa@post.cz
discord: Tereza Š. #1342
'''

import os
import random 
import sys 

from pravidla import pravidla


def pravidla_hry(pravidla: str) -> None: 
    """
    Popis:
    Zobrazi pravidla hry. 

    Parametry:
    :vstupni parametry:
    :pravidla: str
        Text vysvetlujici pravidla hry

    :promenne:
    :oddelovac: str
        Graficky prvek pro lepsi prehlednost obrazovky

    :return:
        Funkce nevraci zadny vystup. 
    """   
    oddelovac = '=' * 50
    print(f'''
    \n{oddelovac}\n
    \nAhoj, zahrajeme si piskvorky?
    \nNez zacneme, mrkni na pravidla hry: 
    \n{pravidla} 
    \n{oddelovac}\n'''
          )


def budeme_hrat(start: str) -> tuple:
    """
    Popis:
    Na zaklade uzivatelskeho vstupu -hrac chce/nechce zahajit hru-
    nastavi hodnoty prommenych pro rizeni behu programu. 

    Parametry:
    :vstupni parametry:
    :start: str
        Uzivatelsky vstup, zahajit hru ano-ne

    :promenne:
    :hrajeme: bool
        Promenna ridici beh hry. True - hra bezi, False - hra je ukoncena
    :zvol_pole: bool
        Promenna, ktera rozhoduje, jestli program vyzve hrace 
        k volbe velikosti hraciho pole. True - program se bude dotazovat,
        False - program se nebude dotazovat

    :return:
        Funkce vraci tuple s promennymi hrajeme, typ bool, a zvol_pole, typ bool. 
    """
    if start == 'A' or start == 'a':
        hrajeme = True
        zvol_pole = True
    else:
        hrajeme = False
        zvol_pole = False
    return (hrajeme, zvol_pole)

 
def zvol_velikost_hraciho_pole(pocet_radku: str) -> tuple:
    """
    Popis:
    Umozni hracum zvolit velikost hraciho pole. Pokud je zadany vstup
    nespravny, pta se na volbu velikosti hraciho pole znovu.  

    Parametry:
    :vstupni parametry:
    :pocet_radku: str
        Uzivatelsky vstup, zvoleny pocet radku hraciho pole 

    :promenne:
    :velikost_pole: int
        Velikost pole je vyjadrena poctem radku hraciho pole.
    :zvol_pole: bool
        Promenna, ktera rozhoduje, jestli program znovu vyzve hrace 
        k volbe velikosti hraciho pole. V pripade nespravneho vstupu zustava
        hodnota promenne True - program znovu vyzve k volbe velikosti hraciho pole. 
        Pri spravnem vstupu je hodnota prepnuta na False - volba velikosti
        hraciho pole je ukoncena. 

    :return:
        Funkce vraci tuple s promennymi velikost_pole, typ int, a zvol_pole, typ bool. 
    """
    if pocet_radku.isdigit() and int(pocet_radku) > 2:
        if int(pocet_radku) > 4:
            print(f'\nHraci pole ma {pocet_radku} radku a {pocet_radku} sloupcu\n')
        else:
            print(f'\nHraci pole ma {pocet_radku} radky a {pocet_radku} sloupce\n')
        velikost_pole = int(pocet_radku)
        zvol_pole = False  
    else:
        print('Chybny vstup. Zadej znova')
        velikost_pole = -1
        zvol_pole = True
    return (velikost_pole, zvol_pole)    


def herni_grid(velikost_pole: int) -> tuple:
    """
    Popis:
    Vytvori prazdne hraci pole, do ktereho se budou vpisovat policka vybrana hracem O 
    a hracem X behem hry. Pocet radku hraciho pole byl zvolen hraci, pocet sloupcu 
    doplni funkce a pocet sloupcu je stejny jako pocet radku. 

    Parametry:
    :vstupni parametry:
    :velikost_pole: int
    Pocet radku hraciho pole zvoleny hraci

    :promenne:
    :grid: list
        Hraci pole, je vytvorene postupnym pridavanim radku az do poctu
        zvoleneho hraci.
    :radek: list
        Jednotlivy radek hraciho pole, je vytvoreny postupnym pridavanim policek
        az do poctu zvoleneho hraci
    :bunka: str
        Jednotlive policko hraciho pole     
   
    :return:
        Funkce vraci tuple s promennymi grid, typ list, a bunka, typ str. 
    """
    grid = []
    for _ in range(velikost_pole):
        radek = []
        for _ in range(velikost_pole):
            bunka = '   '
            radek.append(bunka)
        grid.append(radek)
    return (grid, bunka) 


def planek_hraciho_pole(velikost_pole: int) -> list:
    """
    Popis:
    Vytvori planek hraciho pole, cisla policek slouzi hracum jako napoveda pri volbe 
    jejich tahu. 

    Parametry:
    :vstupni parametry:
    :velikost_pole: int
        Pocet radku hraciho pole zvoleny hraci

    :promenne:
    :planek: list
        Planek hraciho pole, je vytvoreny postupnym pridavanim radku az do poctu
        zvoleneho hraci.
    :radek: list
        Jednotlivy radek hraciho pole, je vytvoreny postupnym pridavanim policek
        (bunek) az do velikosti zvolene hraci
    :bunka: int
        Cislo policka.     
   
    :return:
        Funkce vraci promennou planek, typ list.
    """
    planek = []
    bunka = 1
    for _ in range(velikost_pole):
        radek = []
        for _ in range(velikost_pole):
            if bunka < 10:
                radek.append('  ' + str(bunka))
            else:
                radek.append(' ' + str(bunka))
            bunka += 1
        planek.append(radek)
    return planek


def zobraz_hraci_pole(grid: list, velikost_pole: int) -> None:
    """
    Popis:
    Vytiskne bud planek hraciho pole, nebo vytiskne hraci pole a jeho aktualni
    stav. Zalezi, s jaky argumentem (v parametru grid) je funkce volana

    Parametry:
    :vstupni parametry:
    :grid: list
        Bud planek hraciho pole, nebo aktualni hraci pole.
    :velikost_pole: int
        Pocet radku/sloupcu hraciho pole/planku hraciho pole.

    :promenne:
    :oddelovac: str
        Graficky prvek pro lepsi prehlednost obrazovky
    :index: int
        Pomocna promenna pro postupne vytahovani radku hraciho pole/planku hraciho pole pro tisk.     
    :radek: list
        Radek hraciho pole/planku hraciho pole

    :return:
        Funkce nevraci zadnou promennou.
    """
    oddelovac = '+' + '----' * velikost_pole + '+'
    print(oddelovac)
    for index in range(velikost_pole):
        radek = (grid[index])
        print('|'.join(radek)) 
        print(oddelovac)


def policko_v_gridu(zvolene_policko: int, velikost_pole: int) -> bool:
    """
    Popis:
    Zkontroluje, jestli hracem vybrane policko lezi v hernim poli. 

    Parametry:
    :vstupni parametry:
    :zvolene_policko: int
        Policko vybrane hracem pro polozeni jeho kamene 
    :velikost_pole: int
        Pocet radku/sloupcu hraciho pole    

    :promenne:
    :mimo_grid: bool
        Promenna typu bool, ktera nese informaci jestli vybrane policko
        lezi v hracim poli, nebo je mimo nej

    :return:
        Funkce vraci promennou mimo_grid, typ bool
    """
    if zvolene_policko > velikost_pole ** 2:
        mimo_grid = True
    else:
        mimo_grid = False
    return(mimo_grid)  


def souradnice_policka(velikost_pole: int, zvolene_policko: int) -> tuple:
    """
    Popis:
    Z cisla zvoleneho policka spocita radek a sloupec, ve kterem policko lezi. 

    Parametry:
    :vstupni parametry:
    :velikost_pole: int
        Pocet radku/sloupcu hraciho pole    
    :zvolene_policko: int
        Policko vybrane hracem pro polozeni jeho kamene   

    :promenne:
    :radek: int
        Radek, na kterem lezi hracem vybrane policko. Prvni radek ma index 0
    :sloupec: int
        Sloupec, ve kterem lezi hracem vybrane policko. Prvni sloupec ma index 0   

    :return:
        Funkce vraci tuple obsahujici promenne radek, typ int, a sloupec, typ int

    Priklad:
    >>> zvolene_policko = 5
    >>> velikost_pole = 3
    >>> radek = 5 // 3
    >>> radek = 1
    >>> sloupec = (5 % 3) - 1
    >>> sloupec = 1  
    
    >>> zvolene_policko = 6
    >>> velikost_pole = 3
    >>> radek = (6 - 1) // 3
    >>> radek = 1
    >>> sloupec = 3 - 1
    >>> sloupec = 2  
    """
    radek = zvolene_policko // velikost_pole
    sloupec = (zvolene_policko % velikost_pole)
    if sloupec == 0:
            radek = (zvolene_policko - 1) // velikost_pole
            sloupec = velikost_pole
    sloupec -= 1
    return (radek, sloupec)


def policko_volne(grid: list, radek: int, sloupec: int) -> bool:
    """
    Popis:
    Zkontroluje, jestli hracem vybrane policko je volne.  

    Parametry:
    :vstupni parametry:
    :grid: list
        Aktualni hraci pole.    
    :radek: int
        Radek, na kterem lezi hracem vybrane policko.
    :sloupec: int
        Sloupec, na kterem lezi hracem vybrane policko.       

    :promenne:
    :obsazene: bool 
        Je-li zvolene policko obsazene, je promenna nastavena na hodnotu True.
        Je-li zvolene policko volne, je promenna nastavena na hodnotu False 

    :return:
        Funkce vraci promennou obsazene, typ bool
    """
    if grid[radek][sloupec] == ' x ' or grid[radek][sloupec] == ' o ':
        obsazene = True
    else:
        obsazene = False
    return obsazene 


def zapis_tah(grid: list, radek: int, sloupec: int, hrac: str) -> list:
    """
    Popis:
        Zapisuje tahy hracu do hraciho pole.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :hrac: str
            Symbol hrace, ktery je aktualne na tahu          

        :promenne:
        :grid: list 
            Aktualizovane hraci pole se zapsanym poslednim tahem hracu

        :return:
            Funkce vraci promennou grid, typ list
    """
    grid[radek][sloupec] = ' ' + hrac + ' '
    return grid


def piskvorka_radek_prava(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka v radku vpravo od aktualne zvoleneho policka slepi 
        (aktualne zvolene policko + dve sousedni vpravo) a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if sloupec + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek][sloupec + 1])
    if sloupec + 2 <= (velikost_pole - 1):    
        piskvorka.append(grid[radek][sloupec + 2])
    return piskvorka


def piskvorka_radek_leva(grid: list, radek: int, sloupec: int) -> list:
    """
    Popis:
        Sousedni policka v radku vlevo od aktualne zvoleneho policka slepi 
        (aktualne zvolene policko + dve sousedni vlevo) a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int        

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if sloupec - 1 >= 0:
        piskvorka.append(grid[radek][sloupec - 1])
    if sloupec - 2 >= 0: 
        piskvorka.append(grid[radek][sloupec - 2]) 
    return piskvorka  


def piskvorka_radek_stred(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka vpravo a vlevo v radku od aktualne zvoleneho policka slepi 
        (aktualne zvolene policko + jedno sousedni vlevo + jedno sousedni vpravo) 
        a vytvori z nich novou promennou. 

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if sloupec - 1 >= 0:
        piskvorka.append(grid[radek][sloupec - 1])
    if sloupec + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek][sloupec + 1])
    return piskvorka    


def piskvorka_sloupec_dolni(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka ve sloupci pod aktualne zvolenym polickem slepi 
        (aktualne zvolene policko + dve sousedni pod nim) a vytvori z nich 
        novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek + 1][sloupec])
    if radek + 2 <= (velikost_pole - 1):    
        piskvorka.append(grid[radek + 2][sloupec])
    return piskvorka


def piskvorka_sloupec_horni(grid: list, radek: int, sloupec: int) -> list:
    """
    Popis:
        Sousedni policka ve sloupci nad aktualne zvolenym polickem slepi 
        (aktualne zvolene policko + dve sousedni nad) a vytvori z nich 
        novou promennou. 

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek - 1 >= 0:
        piskvorka.append(grid[radek - 1][sloupec])
    if radek - 2 >= 0: 
        piskvorka.append(grid[radek - 2][sloupec])  
    return piskvorka

   
def piskvorka_sloupec_stred(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka ve slopuci nad a pod aktualne zvolenym polickem slepi 
        (aktualne zvolene policko + jedno sousedni nad + jedno sousedni pod)
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek - 1 >= 0:
        piskvorka.append(grid[radek - 1][sloupec])
    if radek + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek + 1][sloupec])
    return piskvorka


def piskvorka_diagonala_shora_prava(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka v diagonale shora vpravo od aktualne zvoleneho 
        policka slepi (aktualne zvolene policko + dve sousedni vpravo pod) 
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek + 1 <= (velikost_pole - 1) and sloupec + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek + 1][sloupec + 1])
    if radek + 2 <= (velikost_pole - 1) and sloupec + 2 <= (velikost_pole - 1):    
        piskvorka.append(grid[radek + 2][sloupec + 2])
    return piskvorka  


def piskvorka_diagonala_shora_leva(grid: list, radek: int, sloupec: int) -> list:
    """
    Popis:
        Sousedni policka v diagonale shora vlevo od aktualne zvoleneho 
        policka slepi (aktualne zvolene policko + dve sousedni vlevo nad) 
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek -1 >= 0 and sloupec - 1 >= 0:
        piskvorka.append(grid[radek - 1][sloupec - 1])
    if radek - 2 >= 0 and sloupec - 2 >= 0: 
        piskvorka.append(grid[radek - 2][sloupec - 2]) 
    return piskvorka


def piskvorka_diagonala_shora_stred(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka v diagonale shora vlevo a vpravo od aktualne zvoleneho 
        policka slepi 
        (aktualne zvolene policko + sousedni vlevo nad + sousedni vpravo pod) 
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek - 1 >= 0 and sloupec - 1 >= 0:
        piskvorka.append(grid[radek - 1][sloupec - 1])
    if radek + 1 <= (velikost_pole - 1) and sloupec + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek + 1][sloupec + 1]) 
    return piskvorka


def piskvorka_diagonala_zdola_leva(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka v diagonale zdola vlevo od aktualne zvoleneho 
        policka slepi (aktualne zvolene policko + dve sousedni vlevo pod) 
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek + 1 <= (velikost_pole - 1) and sloupec - 1 >= 0:
        piskvorka.append(grid[radek + 1][sloupec - 1])
    if radek + 2 <= (velikost_pole - 1) and sloupec - 2 >= 0:    
        piskvorka.append(grid[radek + 2][sloupec - 2]) 
    return piskvorka


def piskvorka_diagonala_zdola_prava(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka v diagonale zdola vpravo od aktualne zvoleneho 
        policka slepi (aktualne zvolene policko + dve sousedni vpravo nad) 
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek -1 >= 0 and sloupec + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek - 1][sloupec + 1])
    if radek - 2 >= 0 and sloupec + 2 <= (velikost_pole - 1): 
        piskvorka.append(grid[radek - 2][sloupec + 2]) 
    return piskvorka      
    

def piskvorka_diagonala_zdola_stred(grid: list, radek: int, sloupec: int, velikost_pole: int) -> list:
    """
    Popis:
        Sousedni policka v diagonale zdola vlevo a vpravo od aktualne zvoleneho 
        policka slepi 
        (aktualne zvolene policko + sousedni vlevo pod + sousedni vpravo nad) 
        a vytvori z nich novou promennou.  

        Parametry:
        :vstupni parametry:
        :grid: list
            Aktualni hraci pole.    
        :radek: int
            Radek, na kterem lezi hracem vybrane policko.
        :sloupec: int
            Sloupec, na kterem lezi hracem vybrane policko. 
        :velikost_pole: int
            Pocet radku/sloupcu hraciho pole.          

        :promenne:
        :piskvorka: list 
            Sousedni policka hraciho pole slepena do nove promenne 

        :return:
            Funkce vraci promennou piskvorka, typ list
    """
    piskvorka = []
    piskvorka.append(grid[radek][sloupec])
    if radek - 1 >= 0 and sloupec + 1 <= (velikost_pole - 1):
        piskvorka.append(grid[radek - 1][sloupec + 1])
    if radek + 1 <= (velikost_pole - 1) and sloupec - 1 >= 0:
        piskvorka.append(grid[radek + 1][sloupec - 1])    
    return piskvorka    


def je_tam_piskvorka(piskvorka: list, hrac: str) -> bool:
    """
    Popis:
    Otestuje, jestli sousedni policka obsahuji stejny symbol, tj. jestli
    vznikla piskvorka.  

    Parametry:
    :vstupni parametry:
    :piskvorka: list
        Tri sousedni policka v libovolnem smeru vyjmuta z hraciho pole 
        k otestovani.    
    :hrac: str
        Symbol hrace, ktery je aktualne na tahu      

    :promenne:
    :cela_piskvorka: bool 
        Obsahuji-li vsechna policka stejny symbol a ten se shoduje i se symbolem
        hrace, ktery je aktualne na tahu, je promenna nastavena na hodnotu True.
        Neobsahuji-li policka stejny symbol nebo se symboly neshoduji se symbolem
        hrace, ktery je aktualne na tahu, je promenna nastavena na hodnotu False 

    :return:
        Funkce vraci promennou cela_piskvorka, typ bool
    """
    hrac = ' ' + hrac + ' '
    if len(piskvorka) == 3 and piskvorka[0] == piskvorka[1] == piskvorka [2] == hrac:
        cela_piskvorka = True  
    else:
        cela_piskvorka = False
    return cela_piskvorka         


def prepni_hrace(hrac: str) -> str:
    """
    Popis:
    Prepina hrace, ktery je aktualne na tahu.  

    Parametry:
    :vstupni parametry:
    :hrac: str
        Hrac, ktery tahl v prave skoncenem kole. 

    :promenne:
    :hrac: str 
        Aktualizovany hrac. Tento hrac bude na tahu v pristim kole

    :return:
        Funkce vraci promennou hrac, typ str
    """
    if hrac == 'x':
        hrac = 'o'
    elif hrac == 'o':
        hrac = 'x'
    return hrac


def je_pole_zaplnene(grid: list, volna_bunka: str) -> bool:
    """
    Popis:
    Prochazi hraci pole policko po policku a kontroluje, jestli uz nejsou 
    obsazena vsechna policka hraciho pole. Vraci promennnou zaplnene_pole,
    ktera vstupuje do rozhodovani o dalsim pokracovani, ci ukonceni programu.

    Parametry:
    :vstupni parametry:
    :grid: list
        Aktualni hraci pole.    
    :volna_bunka: str
        String reprezentujici prazdne hraci policko
  
    :promenne:
    :zaplnene_pole: bool 
        Promenna je na zacatek nastavena na hodnotu True.
        Narazi-li funkce na prazdne policko, prepne promennou 
        a hodnotu False. 
        
    :return:
        Funkce vraci promennou zaplnene_pole, typ bool
    """
    zaplnene_pole = True
    for radek in grid:
        for policko in radek:
            if policko == volna_bunka:
                zaplnene_pole = False
                break
    return zaplnene_pole        


def hraj_piskvorky(): 
    oddelovac = '-' * 50

    pravidla_hry(pravidla) 

    start = input('Jdeme hrat? A/N: ')
    hrajeme, zvol_pole = budeme_hrat(start)  

    while zvol_pole: 
        pocet_radku = input('\nZadej pocet radku hraciho pole: ')    
        velikost_pole, zvol_pole = zvol_velikost_hraciho_pole(pocet_radku)

    if hrajeme:
        grid, volna_bunka = herni_grid(velikost_pole)
        planek = planek_hraciho_pole(velikost_pole)
        hrac = random.choice(['x', 'o'])   
        
    while hrajeme:
        print(f'{oddelovac} \n\n Planek hraciho pole\n')
        zobraz_hraci_pole(planek, velikost_pole)

        print(f'\n{oddelovac} \n\n Aktualni hraci pole\n')
        zobraz_hraci_pole(grid, velikost_pole)
        print(f'\n{oddelovac}\n')

        print(f'\nNa rade je hrac {hrac.upper()}') 
   
        zvolene_policko = input('Zvol policko: ')      
        if zvolene_policko =='Q' or zvolene_policko =='q':
            print(f'\n{oddelovac} \nKonec hry \n{oddelovac} \n')
            hrajeme = False
            break
        elif zvolene_policko.isdigit():
            zvolene_policko = int(zvolene_policko)
        else:
            print('\nZadej cele cislo\n')
            continue       

        policko_mimo_grid = policko_v_gridu(zvolene_policko, velikost_pole)
        if policko_mimo_grid:
            print('\nZvolene policko je mimo grid. Zadej tah znovu \n')
            continue

        radek, sloupec = souradnice_policka(velikost_pole, zvolene_policko)

        obsazene_policko = policko_volne(grid, radek, sloupec)
        if obsazene_policko:
            print('\nZvolene policko je obsazene. Hraje souper \n')
            hrac = prepni_hrace(hrac) 
            continue

        grid = zapis_tah(grid, radek, sloupec, hrac)

        piskvorka = piskvorka_radek_prava(grid, radek, sloupec, velikost_pole)
        je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_radek_leva(grid, radek, sloupec)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_radek_stred(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)

        if not je_piskvorka:
            piskvorka = piskvorka_sloupec_dolni(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_sloupec_horni(grid, radek, sloupec)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_sloupec_stred(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)

        if not je_piskvorka:
            piskvorka = piskvorka_diagonala_shora_prava(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_diagonala_shora_leva(grid, radek, sloupec)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_diagonala_shora_stred(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)

        if not je_piskvorka:
            piskvorka = piskvorka_diagonala_zdola_leva(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_diagonala_zdola_prava(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)
        if not je_piskvorka:
            piskvorka = piskvorka_diagonala_zdola_stred(grid, radek, sloupec, velikost_pole)
            je_piskvorka = je_tam_piskvorka(piskvorka, hrac)  
                      
        if je_piskvorka:
            hrajeme = False
            if sys.platform == 'linux':
                os.system('clear')
            else:     
                os.system('cls')
            print(f'\n{oddelovac} \n\nVyhral hrac {hrac.upper()} \n' )
            zobraz_hraci_pole(grid, velikost_pole)

        remiza = je_pole_zaplnene(grid, volna_bunka) 
        
        if remiza and not je_piskvorka:
            hrajeme = False
            if sys.platform == 'linux':
                os.system('clear')
            else:     
                os.system('cls')
            print(f'\n{oddelovac} \n\nHra skoncila remizou \n')
            zobraz_hraci_pole(grid, velikost_pole)          

        if hrajeme:
            hrac = prepni_hrace(hrac)
            if sys.platform == 'linux':
                os.system('clear')
            else:     
                os.system('cls')  
    else:
        print(f'\n{oddelovac} \nKonec hry \n{oddelovac} \n')

if __name__ == '__main__':
   
    hraj_piskvorky()