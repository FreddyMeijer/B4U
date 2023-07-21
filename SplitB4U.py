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

original = r'PATH_TO_FILE'
rowsPerFile = 10

lastSlashIndex = original.rfind('\\')
lastDotIndex = original.find('.', lastSlashIndex)

new = original[lastSlashIndex + 1:lastDotIndex]

createFiles(original, new, rowsPerFile)