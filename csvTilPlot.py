# -*- coding: utf-8 -*-
"""
Dette er ett av to skjelettprogram for Python-delen av semesteroppgaven i DAT111 H2024.

Fullfør denne filen basert på kravene og strukturen spesifisert her og i pdf-filen på Canvas.

Merk: indenteringen som er brukt på kommentarene indikerer hvilket nivå koden dere fyller inn skal ligge på.

Fyll inn informasjonen under.
Gruppe: 5

Navn på gruppemedlemmer:
Filip Marek Bartczak
Ketil Andre Trollvang
Marius Samdal-Hanssen
Nina Mæland Polden
Ola Garborg 

"""

from matplotlib import pyplot as plt
import csv  

### Funksjon som styrer flyten i programmet ###
def main():
    # Bruker importerBesoekertall-funksjonen til å opprette en liste bestående av alle radene
    # i csv-filen og lagre denne i en variabel.
    csvliste = importerBesoekertall("C:\\Users\\Olaga\\Downloads\\besoekerstatistikk.csv")
  # Kaller på funksjonen for å hente data
    print(csvliste)  # Sjekker innholdet i listen
    # Gå gjennom alle radene i csvliste, hent ut verdier, finn anbefalte tidsrom og plot grafer.
    for rad in csvliste[1:]:  
        dag = rad[0]
        y = list(map(int, rad[1:]))

        # Utfør et kall på anbefalteTidsrom-funksjonen med dag, liste over tidspunkt, liste over besøkende, og en grenseverdi
        anbefalte_tidsrom = anbefalteTidsrom(dag, list(range(len(y))), y, grenseverdi=50)
        print(f"Anbefalte tidsrom for {dag}: {anbefalte_tidsrom}")

        # Utfør et kall på plotGraf-funksjonen med verdiene for x- og y-aksen samt navnet på dagen
        plotGraf(list(range(len(y))), y, dag)

### Funksjon som importerer fil ved hjelp av csv-biblioteket ###
def importerBesoekertall(filnavn):
    # Opprett en tom liste som skal holde på verdiene som blir lest fra csv-filen.
    data = []
    
    # Åpner filen for lesing.
    with open(filnavn, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Hopper over header-raden hvis den finnes
        for rad in reader:
            data.append(rad)
    
    # Returner den ferdige listen med innholdet fra csv-filen.
    return data
   

### Funksjon som plotter en graf ved hjelp av matplotlib ###
def plotGraf(x, y, navn):
    # Opprett fire grenseverdier som spesifiserer lite, medium, høyt og veldig høyt besøkstall.
    lite_besok = 2      # Eksempelverdi for lite besøkstall
    medium_besok = 8    # Eksempelverdi for medium besøkstall
    hoyt_besok = 15     # Eksempelverdi for høyt besøkstall
    veldig_hoyt_besok = 20  # Eksempelverdi for veldig høyt besøkstall
    
    # Spesifiserer fargene i plottet
    barcolor = [
        {'green': verdi <= lite_besok, 'yellow': lite_besok < verdi <= medium_besok,
         'orange': medium_besok < verdi <= hoyt_besok, 'red': verdi > veldig_hoyt_besok}[True]
        for verdi in y
    ]

    # Definerer barene i plottet
    plt.bar(
        x=x, height=y, color=barcolor, edgecolor='black', linewidth=1, width=0.8
    )
    plt.xlabel("Tidspunkt")          # Navn på x-aksen
    plt.ylabel("Antall besøkende")    # Navn på y-aksen
    plt.title(f"Besøkstall i Læringslab - {navn}")  # Tittel på grafen med navnet på dagen
    
    # Lagrer plottet
    plt.savefig(f"besokstall_plot_{navn}.png")
    plt.show()  # Viser plottet i IDE

### Funksjon som finner og skriver ut anbefalte tidsrom for besøk ###
def anbefalteTidsrom(dag, tidspunktliste, besoekendeliste, grenseverdi):
    # Oppretter variabler for å holde på tidsrom og for å mellomlagre start- og sluttverdi for tidsrom.
    anbefalte_tidsrom = []
    
    # Variabler for å midlertidig lagre start- og sluttverdi for tidsrom
    start = None
    slutt = None
    
    # Går gjennom alle tidspunktene og tilhørende besøkstall for å sjekke om de er del av et anbefalt tidsrom
    for i in range(len(besoekendeliste)):
        tidspunkt = tidspunktliste[i]
        besok = besoekendeliste[i]
        
        if besok < grenseverdi:
            # Start nytt tidsrom hvis `start` ikke er satt
            if start is None:
                start = tidspunkt
            slutt = tidspunkt  # Oppdater slutt til det nåværende tidspunktet
        else:
            # Hvis besøkstallet er over grenseverdien, avslutt tidsrommet hvis det er startet
            if start is not None:
                anbefalte_tidsrom.append((start, slutt))
                start = None  # Tilbakestill start for å markere slutten på tidsrommet

    # Legg til det siste tidsrommet hvis det ikke er avsluttet ved slutten av listen
    if start is not None:
        anbefalte_tidsrom.append((start, slutt))
    
    # Skriv ut anbefalte tidsrom for dagen
    print(f"Anbefalte tidsrom for {dag}: {anbefalte_tidsrom}")
    return anbefalte_tidsrom

# Kaller på main-metoden til slutt
if __name__ == "__main__":
    main()
