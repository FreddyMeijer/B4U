# B4U Tools
Welcome to the B4U tools repo. I am Freddy Meijer and at the time business engineer at Leiden. In a Betty Blocks application we retrieve information from City Control (Sigmax). The data of City Control is in B4U format. A custom fileformat created by Sigmax. B4U is fixed lenght so we can translate that to a readable format (table). In this repo you find serveral tools to work with B4U files.

## .gitignore
The gitignore file states that .b4u files will not be uploaded through git. The information in a b4u file is personal en thereby protected under GDPA regulations. So the files itself should never be uploaded on GitHub.

## b4u.code-snippets
In Visual Studio Code you can create a snippet. If you type html for instance, VS Code will autocomplete the HTML file. This can also be done with a B4U snippet. This code provides an empty b4u file, but with header and footer records.

## ConvertB4UToCSV
To run this script pandas should be installed. The user is asked to select a b4u file through a the file-explorer. With this variable, the variable *locationTarget* will be created. This two are the same, except for the extention (b4u will be changed to csv).

The file in *locationSource* is opend and all lines in the file will be looped through, except the first and last line which are the header and tailline of the file which does not include data we want to extract. Furthermore we create an empty array (*data*) which we will fill in the following for-loop

In the for-loop every line from the source is cut into seperate variables. These variables are appended to the array *data*. The variable names are in Dutch for this file is used in a Dutch environment (the CSV). The code is in English. 

When the loop is at an end, the array (*data*) is converted to a pandas dataframe (*df*). This dataframe is then saved as a CSV on the targetlocation (stored in *locationTarget*).

## SplitB4U
The Python code is build up in two parts. The first is a function in which the sourcefile (*original*) is cut up in serveral smaller files. The second part is the piece of code which executes the function.

The function reads the original B4U file. The first row (header) and the last row (footer) are saved in the variables with the names *header* en *footer* (.pop()). The total amount of lines is devided with the *rowsPerFile*. This makes the *totalFiles* 

When we know the total amount of files, we can loop through these files. The total amount of lines is determined by the calculation *lines[i * rowsPerFile: (i + 1) * rowsPerFile]*. Now we know which lines of the original should be transfered to the new file, we append the footer and insert the header before the first line. 

This will be saved in an outputfile with the same name but with the counter attached. So when the original file is *freddy.b4u* then the first new file will be *freddy_1.b4u*. The result is printed to terminal.

When we use the function, we need to give the total path (including the file itself) in *original* through a filedialog. Furthermore we must indicate how many lines the new files should have (*rowsPerFile* in codeline 21). This is asked through the terminal (input). Then we cut the name of the file by saving the characters between the last slash and before the last dot. This variable (*new*) is needed for the new filesnames.

## ConvertReportToB4U
From PAL21 we recieve a report. This report is downloaded from the model import. Through a filedialog the user selects the csv report from PAL21. This is translated to a valid B4U file. That file is saved at the same location as the selected csv file. 