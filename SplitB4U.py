import tkinter as tk
from tkinter import filedialog

def selectFile():
    File=filedialog.askopenfilename(
        title="Selecteer het B4U File",
        filetypes=[("B4U Bestanden","*.b4u"),("Alle bestanden","*.*")]
    )
    if File:
        return File

def createFiles(original, new, rowsPerFile):
    with open(original, 'r') as f:
        lines = f.readlines()

    header = lines.pop(0)
    footer = lines.pop()

    totalFiles = (len(lines) // rowsPerFile) + 1

    for i in range(totalFiles):
        fileLines = lines[i * rowsPerFile: (i + 1) * rowsPerFile]
        fileLines.insert(0, header)
        fileLines.append(footer)
        output_file = f"{new}_{i + 1}.b4u"
        with open(output_file, 'w') as f_out:
            f_out.writelines(fileLines)

        print(f"File created: {output_file}")

original = selectFile()
rowsPerFile = input ("Hoeveel regels moeten er per bestand worden gegenereerd? ")
rowsPerFile = int(rowsPerFile)

lastSlashIndex = original.rfind('\\')
lastDotIndex = original.find('.', lastSlashIndex)

new = original[lastSlashIndex + 1:lastDotIndex]

createFiles(original, new, rowsPerFile)