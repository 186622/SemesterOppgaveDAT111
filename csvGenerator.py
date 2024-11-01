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

### Importer nødvendige bibliotek ###
import csv
import random

### Generer csv-fil med csv-biblioteket ###
# Åpne eksisterende fil/opprett ny med det spesifiserte navnet, i skrivemodus.
with open('besoekerstatistikk.csv', 'w', newline='') as fil:
    # Opprett en referanse til csv-biblioteket sin skriverfunksjon med den åpnede filen som argument.
    csvWriter = csv.writer(fil)

    # Lag header-raden som skal bestå av tekststrengen "Dag" og alle tidspunktene i åpningstiden.
    header = ['Dag', 9,10,11,12,13,14,15,16,17,18]

    # Skriv header-raden til filen ved hjelp av skriverfunksjonen.
    csvWriter.writerow(header)

    # Lag en liste av alle dagene det er åpent på Læringslab.
    days = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']

    # Vi skal nå generere besøkstall per dag, med tilfeldig variasjon, og skrive de til fil.
    # Bruk en for-løkke til å gå gjennom alle dagene i listen over dager.
    for day in days:
    # Opprett en ny liste som skal representere dagens besøkstall.
    # Legg inn navnet på dagen som startelement.
        row = [day]

    # Opprett to variabler som holder på start- og sluttverdi for det tilfeldige intervallet.
        start, end = 4, 10

        # Bruk en for-løkke til å gå gjennom alle tidspunktene i åpningstiden ved hjelp av range()-funksjonen.
        for time in range(9, 19):
            # Opprett en tilfeldig verdi ved hjelp av random.sample(). Som argument til funksjonen
            # gir dere range() med start- og slutt-verdier som dere har lagret i variabler tidligere.
            # random.sample() returnerer en liste (i dette tilfellet av størrelse 1), hent ut den
            # første verdien fra listen.
            randomValue = random.sample(range(start, end), 1)[0]

            # Legg til den nye verdien i listen for dagens besøkstall.
            row.append(randomValue)

            # Bruk en if-elif-else-struktur for å endre på start- og sluttverdi for det tilfeldige intervallet.
            # Målet er at det skal resultere i en naturlig fordeling av besøkende, for eksempel normalfordelt eller
            # med en topp før og en etter lunsjtid.

            if time < 11:
                start, end = start + 11 - time, end + 11 - time
            elif time == 11:
                start, end = 4, 8
            elif time == 12:
                start, end = 10, 16
            elif 12 < time <= 13:
                start, end = start + 14 - time, end + 14 - time
            else:
                start, end = start - (-1 * (14 - time)), end - -1 * (14 - time)
        # Skriv raden til fil.

        csvWriter.writerow(row)