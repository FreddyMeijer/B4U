# Auteur: Freddy Meijer Functioneel beheerder PAL21
# Datum: 29-05-2023
# Titel: Opknippen B4U bestand

# Het komt voor in PAL21 dat grote B4U bestanden niet juist ingelezen worden. Deze knippen we handmatig op.
# In deze code doet Python dat voor ons. Je kan opgeven hoeveel regels er per bestand opgenomen moeten worden.
# Op dit moment staat het in de code op 10 regels. 30 is te adviseren. 

# Eerst definieren we de code als functie (def) met 3 variabelen:
# - orgineel: Hier definieer je het pad en het bestand dat je op wilt knippen
# - rijenperbestand: Hierin geef je aan hoeveel inhoudelijke regels er per bestand moeten komen
# - nieuw: Hier definieer je hoe de nieuwe bestanden moeten heten. Let wel: De telling wordt al geregeld en de naam ook

def maak_bestanden(orgineel, nieuw, RijenPerBestand):
    with open(orgineel, 'r') as f:
        regels = f.readlines()

    #De eerste en laatste regel hoeven niet meegenomen te worden. Dus die 'verwijderen' we uit de collectie
    eersteRegel = regels.pop(0)
    laatsteRegel = regels.pop()

    #aantalBestanden bepaalt hoeveel bestanden aangemaakt moeten worden. Dit is afgerond naar beneden. Dus we doen er 1 bij om het laatste beetje mee te kunnen nemen.
    aantalBestanden = (len(regels) // RijenPerBestand) + 1

    for i in range(aantalBestanden):
        bestandRegels = regels[i * RijenPerBestand: (i + 1) * RijenPerBestand]

        #De eerste en laatste regel moeten toegevoegd worden aan het bestand
        bestandRegels.insert(0, eersteRegel)
        bestandRegels.append(laatsteRegel)

        #Het bestand zelf moet ook aangemaakt worden.
        output_file = f"{nieuw}_{i + 1}.b4u"
        with open(output_file, 'w') as f_out:
            f_out.writelines(bestandRegels)

        print(f"Bestand aangemaakt: {output_file}")

#Uitvoer:
orgineel = r'<<Pad_naar_B4U_bestand>>'
RijenPerBestand = 10

laatsteSlashIndex = orgineel.rfind('\\')
laatstePuntIndex = orgineel.find('.', laatsteSlashIndex)

nieuw = orgineel[laatsteSlashIndex + 1:laatstePuntIndex]

maak_bestanden(orgineel, nieuw, RijenPerBestand)