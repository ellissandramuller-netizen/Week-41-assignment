# Task 1 

# Funksjon som tar inn en gitt liste og oppretter en tom liste for sortering
def flatten_list(nested_list):
    flattened_list = []

    # Sjekker om elementet i listen er en indre liste eller tuple
    for n in nested_list:
        if isinstance(n, (list, tuple)):
            flattened_list.extend(flatten_list(n))  # Flater ut indre lister/tupler rekursivt
        else:
            flattened_list.append(n) # Hvis FALSE så legges elementet til i den tomme lista

    return flattened_list # Returnerer den flate listen

# Task 2
# Definerer hvilken encoding hver logfil må ha 
file_encodings = {
    "log_1.txt": "utf-8",
    "log_2.txt": "utf-8-sig",
    "log_3.txt": "utf-16",
    "log_4.txt": "latin-1"
}

# Definer funksjon og opprett en tom liste for log-linjene i alle filene
def sort_error_logs(encodings):

    log_lines = []

    # Iterering for hver linje i gitt fil 
    for filename, encoding in encodings.items():
        with open(filename, 'r', encoding=encoding) as file:
            content = file.readlines()          # Lagrer linjene som en variabel
            for line in content:                
                if line.startswith("["):        # Henter ut linjene som starter med [
                    log_lines.append(line)      # Legges til i tom liste

    # Oppretter ny fil og skriver inn alle linjene 
    with open('combined_lines.txt', 'w', encoding='utf-8-sig') as file:
        for line in log_lines:
            file.write(line)

sort_error_logs(file_encodings) # Kalle funksjonen

# AI summary:

"""
Jeg brukte ChatGPT som en veileder under arbeidet med oppgavene. 
Vi jobbet steg for steg, der jeg selv skrev koden og fikk forklaringer, 
hint og tilbakemeldinger underveis.

Task 1 – Recursion and flattening:
Jeg fikk hjelp til å forstå hvordan rekursjon fungerer, hvordan en 
funksjon kan kalle seg selv, og forskjellen mellom .append() og .extend(). 
Jeg stilte spørsmål om hvordan jeg kunne sjekke om et element var en liste 
eller tuple ved hjelp av isinstance(). Jeg skrev funksjonen flatten_list() 
selv og testet den med ulike typer nøstede lister.

Task 2 – File handling and encoding:
Jeg fikk veiledning om filhåndtering og ulike tegnkodinger, blant annet 
UTF-8, UTF-16, Latin-1 og UTF-8 med BOM. Jeg stilte spørsmål om 
hvordan jeg kunne lese filer med forskjellige encodings, bruke en dictionary 
til å lagre filnavn og tilhørende encoding, og filtrere ut hele linjer som 
starter med [.

Da programmet bare fant 7 av 8 forventede logglinjer, hjalp ChatGPT 
meg med feilsøking ved å foreslå repr(). Vi oppdaget at log_2.txt inneholdt 
et BOM-tegn, og jeg rettet dette ved å bruke utf-8-sig.

Jeg skrev deretter koden som samlet logglinjene og lagret dem i en ny 
tekstfil med riktig encoding. Jeg fikk også hjelp til å organisere 
koden i en funksjon, forstå forskjellen mellom parametere og argumenter, 
og forbedre kommentarene mine.

Git og GitHub:
Jeg fikk også veiledning i bruk av Git, blant annet commits, push til 
GitHub og hvordan jeg kunne løse en konflikt mellom lokal og ekstern 
repository-historikk.
"""