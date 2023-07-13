# B4U Git

Welkom op de B4U Git. Ik ben Freddy Meijer en ik ten tijde van het schrijven van dit bestand functioneel applicatie beheerder bij de gemeente Leiden. 

## Inleiding

Vanuit Sigmax City Control wordt een B4U bestand gedumpt. Deze moet ingelezen worden in PAL21. Echter: Soms is het nodig om analyses te doen op het B4U bestand of om andere bewerkingen te doen. Alle (Python) code die hiervoor nodig is, staat in deze repo

## Converteer_B4U_bestand.py

Op regel 11 dient het volledige bestandspad opgenomen te worden van het B4U bestand. Dit pad wordt tussen de quotes geplaatst. Vervolgens wordt het B4U bestand in een pandas dataframe geplaatst en gedumpt naar csv. Op deze manier kan je sneller en gemakkelijker via een spreadsheet programma analyses doen.

## Splits_B4U_bestand.py

Het kwam voor dat PAL21 de hoeveelheid regels uit het B4U Bestand niet aankon. Deze code pakt het B4U bestand en knipt deze in kleinere blokken. Op regel 40 wordt het pad naar het grote B4U bestand gedefinieerd. In regel 41 kan je aangeven hoe groot de nieuwe bestanden moeten worden. Dus met andere woorden: Als je een basisbestand hebt van 100 regels en je laat de variabele RijenPerBestand op 10 staan, zullen er 10 bestanden gecreerd worden.

## rapportNaarB4U.py

PAL21 slaat de bestanden niet op zoals ze binnen komen. Echter het B4U bestand wordt als multiline tekst opgeslagen in de importregel. Hierop is een PAL21 rapportage geschreven. Dit rapport bevat echter lege regels. Deze code pakt het CSV rapport op en doorloopt deze regel voor regel. Lege regels en kop- en voetregels worden verwijderd. Hierna wordt een kop- en voetregel toegevoegd en dan heb je een mega B4U bestand.

## b4u.code-snippets

In Visual Studio Code is het mogelijk om een snippet aan te maken. Dit is een soort sneltoets. Met deze snippet kan je een voorloop- en sluitrecord voor een B4U bestand direct genereren zonder na te hoeven denken over de posities.