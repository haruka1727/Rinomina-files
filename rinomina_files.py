import os

# Input da tastiera
nome_serie = input("Inserisci il nome della serie: ").strip().replace(" ", "_")
stagione = input("Inserisci il numero della stagione: ").zfill(2)
episodio_iniziale = int(input("Inserisci il numero dell'episodio iniziale: "))

# Percorso della cartella dei file
cartella = "files"
if not os.path.exists(cartella):
    print(f"La cartella '{cartella}' non esiste.")
    exit()

# Ottieni tutti i file nella cartella (escludendo eventuali sottocartelle)
file_list = sorted([
    f for f in os.listdir(cartella)
    if os.path.isfile(os.path.join(cartella, f))
])

# Rinomina
episodio = episodio_iniziale
for file in file_list:
    nome_base, estensione = os.path.splitext(file)
    nuovo_nome = f"{nome_serie} S{stagione}E{str(episodio).zfill(2)}{estensione}"
    
    # Rinomina effettiva
    src = os.path.join(cartella, file)
    dst = os.path.join(cartella, nuovo_nome)
    
    os.rename(src, dst)
    print(f"Rinominato: {file} -> {nuovo_nome}")
    
    episodio += 1
