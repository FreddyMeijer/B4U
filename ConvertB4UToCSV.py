import pandas as pd
import tkinter as tk
from tkinter import filedialog

def selectFile():
    File=filedialog.askopenfilename(
        title="Selecteer het B4U File",
        filetypes=[("B4U Bestanden","*.b4u"),("Alle bestanden","*.*")]
    )
    if File:
        return File

locationSource = selectFile()
locationTarget = locationSource.replace('.b4u', '.csv')

with open(locationSource, 'r') as f:
    lines = f.readlines()[1:-1]

data = []

for line in lines:
    recordidentifier = line[0:2].strip()
    datum = line[2:10].strip()
    tijd = line[10:14].strip()
    controleursnummer = line[14:29].strip()
    soortVoertuig = line[29:31].strip()
    land = line[31:33].strip()
    kenteken = line[33:44].strip()
    merk = line[44:64].strip()
    kleur = line[64:71].strip()
    catB = line[71:72].strip()
    feit = line[72:80].strip()
    kosten = line[80:97].strip()
    belasting = line[97:113].strip()
    klemkosten = line[113:129].strip()
    www = line[129:132].strip()
    toelichting = line[132:252].strip()
    omschrijving = line[252:372].strip()
    geseponeerd = line[372:401].strip()
    naheffingsnummer = line[401:411].strip()
    if naheffingsnummer.startswith("000"):
        naheffingsnummer = naheffingsnummer[3:]
    straat = line[411:436].strip()

    data.append([recordidentifier, datum, tijd, controleursnummer, soortVoertuig, land, kenteken, merk, kleur, catB,
                feit, kosten, belasting, klemkosten, www, toelichting, omschrijving, geseponeerd, naheffingsnummer, straat])

df = pd.DataFrame(data, columns=['recordidentifier', 'datum', 'tijd', 'controleursnummer', 'soortVoertuig',
                                 'land', 'kenteken', 'merk', 'kleur', 'catB',
                                 'feit', 'kosten', 'belasting', 'klemkosten',
                                 'www', 'toelichting', 'omschrijving', 'geseponeerd', 'naheffingsnummer', 'straat'])

# Print het dataframe naar CSV

df.to_csv(locationTarget, index=False)
print(f"File saved in: {locationTarget}")