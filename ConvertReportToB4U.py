import tkinter as tk
from tkinter import filedialog

def selectFile():
    File=filedialog.askopenfilename(
        title="Selecteer het B4U File",
        filetypes=[("CSV Bestanden","*.csv"),("Alle bestanden","*.*")]
    )
    if File:
        return File

def rapportNaarB4U(rapport):
    b4u = rapport.rsplit('.', 1)[0] + '.b4u'
    with open(rapport, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(b4u, 'w', encoding='utf-8') as file:
        file.write('01 TRDLC PHS4U 0000000000        20230522074439                                                                                                                                                                                                                                                                                                                                                                                                                                                                     '+ '\n')
        for line in lines:
            line = line.strip()

            if line.startswith(('inhoud', '"01', '99EINDE','"')):
                continue
            else:
                file.write(line + '\n')
        file.write('99EINDE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ')

    print("Bestand aangemaakt op locatie: " + b4u)

rapportNaarB4U(selectFile())