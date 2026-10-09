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
