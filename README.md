# B4U Tools
Welcome to the B4U tools repo. I am Freddy Meijer and at the time business engineer at Leiden. In a Betty Blocks application we retrieve information from City Control (Sigmax). The data of City Control is in B4U format. A custom fileformat created by Sigmax. B4U is fixed lenght so we can translate that to a readable format (table). In this repo you find serveral tools to work with B4U files.

## .gitignore
The gitignore file states that .b4u files will not be uploaded through git. The information in a b4u file is personal en thereby protected under GDPA regulations. So the files itself should never be uploaded on GitHub.

## b4u.code-snippets
In Visual Studio Code you can create a snippet. If you type html for instance, VS Code will autocomplete the HTML file. This can also be done with a B4U snippet. This code provides an empty b4u file, but with header and footer records.

## ConvertB4UToCSV
To run this script pandas should be installed. In line 3, you state the path to the location of the file (variable *locationSource*). This includes the file itself. With this variable, the variable *locationTarget* will be created. This two are the same, except for the extention (b4u will be changed to csv).

The file in *locationSource* is opend and all lines in the file will be looped through, except the first and last line which are the header and tailline of the file which does not include data we want to extract. Furthermore we create an empty array (*data*) which we will fill in the following for-loop

In the for-loop every line from the source is cut into seperate variables. These variables are appended to the array *data*. The variable names are in Dutch for this file is used in a Dutch environment (the CSV). The code is in English. 

When the loop is at an end, the array (*data*) is converted to a pandas dataframe (*df*). This dataframe is then saved as a CSV on the targetlocation (stored in *locationTarget*).

## Splits_B4U_bestand.py

Het kwam voor dat PAL21 de hoeveelheid regels uit het B4U Bestand niet aankon. Deze code pakt het B4U bestand en knipt deze in kleinere blokken. Op regel 40 wordt het pad naar het grote B4U bestand gedefinieerd. In regel 41 kan je aangeven hoe groot de nieuwe bestanden moeten worden. Dus met andere woorden: Als je een basisbestand hebt van 100 regels en je laat de variabele RijenPerBestand op 10 staan, zullen er 10 bestanden gecreerd worden.

## rapportNaarB4U.py

PAL21 slaat de bestanden niet op zoals ze binnen komen. Echter het B4U bestand wordt als multiline tekst opgeslagen in de importregel. Hierop is een PAL21 rapportage geschreven. Dit rapport bevat echter lege regels. Deze code pakt het CSV rapport op en doorloopt deze regel voor regel. Lege regels en kop- en voetregels worden verwijderd. Hierna wordt een kop- en voetregel toegevoegd en dan heb je een mega B4U bestand.

## b4u.code-snippets

In Visual Studio Code is het mogelijk om een snippet aan te maken. Dit is een soort sneltoets. Met deze snippet kan je een voorloop- en sluitrecord voor een B4U bestand direct genereren zonder na te hoeven denken over de posities.