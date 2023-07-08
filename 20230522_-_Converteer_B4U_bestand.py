# Auteur: Freddy Meijer Functioneel beheerder PAL21
# Datum: 22-05-2023
# Titel: Omzetten B4U bestand

# Een B4U bestand is een fixed lenght bestand en derhalve slecht te lezen. 
# In onderstaand script wordt het bestand van B4U omgezet naar een CSV bestand met dezelfde naam. 
# Er is feitelijk maar een variabele die je hoeft te vullen en dat is locatieBron op regel 11.

import pandas as pd

locatieBron = r'<<Pad_naar_B4U_bestand>>'

locatieDoel = locatieBron.replace('.b4u', '.csv')

# Open het bestand
with open(locatieBron, 'r') as f:
    # We willen het voorloop- en sluitrecord niet importeren. Dus we lezen vanaf regel 1 tot en met de laatste regel -1
    regels = f.readlines()[1:-1]

# definieer een lege array die we later gaan vullen.
rijen = []

# doorloop iedere regel en vul de variabelen door delen uit de regel te halen (.strip)
for regel in regels:
    recordidentifier = regel[0:2].strip()
    datum = regel[2:10].strip()
    tijd = regel[10:14].strip()
    controleursnummer = regel[14:29].strip()
    soortVoertuig = regel[29:31].strip()
    land = regel[31:33].strip()
    kenteken = regel[33:44].strip()
    merk = regel[44:64].strip()
    kleur = regel[64:71].strip()
    catB = regel[71:72].strip()
    feit = regel[72:80].strip()
    kosten = regel[80:97].strip()
    belasting = regel[97:113].strip()
    klemkosten = regel[113:129].strip()
    www = regel[129:132].strip()
    toelichting = regel[132:252].strip()
    omschrijving = regel[252:372].strip()
    geseponeerd = regel[372:401].strip()
    naheffingsnummer = regel[401:411].strip()
    if naheffingsnummer.startswith("000"):
        naheffingsnummer = naheffingsnummer[3:]
    straat = regel[411:436].strip()

    # Alle variabelen hierboven kunnen als veld toegevoegd worden aan de array (let op: Dit is de vulling van de rijen)
    rijen.append([recordidentifier, datum, tijd, controleursnummer, soortVoertuig, land, kenteken, merk, kleur, catB,
                 feit, kosten, belasting, klemkosten, www, toelichting, omschrijving, geseponeerd, naheffingsnummer, straat])

# Nu maken we een dataframe met kolomkoppen met daaronder alle rijen
df = pd.DataFrame(rijen, columns=['recordidentifier', 'datum', 'tijd', 'controleursnummer', 'soortVoertuig',
                                 'land', 'kenteken', 'merk', 'kleur', 'catB',
                                 'feit', 'kosten', 'belasting', 'klemkosten',
                                 'www', 'toelichting', 'omschrijving', 'geseponeerd', 'naheffingsnummer', 'straat'])

# Print het dataframe naar CSV

df.to_csv(locatieDoel, index=False)
print(f"Bestand aangemaakt: {locatieDoel}")