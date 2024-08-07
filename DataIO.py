
import pandas as pd
import openpyxl
#Importiert Pandas Bibliothek
import time
#Imontiert das Zeitmodul
import os

global contentpathdata
global contentpathteams
global teamsbefehl
global teamsbefehlzeile
#Definiert die verschiedenen Variabeln
teamsbefehlzeile = "content"
contentpathdata = "C:\\Temp\\Befehle.xlsx"
contentpathteams = "C:\\Users\\M320389\\OneDrive - MerckGroup\\Documents\\Pop-ups.txt"
teamsbefehl = "kein befehl"
#Definiert welche Excel Datei zu welcher Variabel gehört


def readexcellinedata():
    #Definiert die Funktion readexcellinedata
    global teamsbefehl,teamsbefehlzeile,contentpathdata
    #Read the Excel file
    data = pd.read_excel(contentpathdata)
    
    teamsbefehlzeile = data[data['reference'].str.contains(teamsbefehl, case=False, na=False)]
    #Filtert die Daten in der Spalte reference der Tabelle und speichert das Ergebniss in die Teamsbefehlzeile
    
    
    print("data: ",data)
    print("teamsbefehlzeile: ",teamsbefehlzeile)
    
def readexcellineteams():
    global teamsbefehl, contentpathteams
    #Die Variablen Teamsbefehl und Contentpath werden als Global definiert
    #Read the Excel file
    
    # Open the file in read mode
    
    if os.path.exists(contentpathteams):
        with open(contentpathteams, 'r') as file:
        # Read the entire file content
            data = file.read()
            teamsbefehl = data
        os.remove(contentpathteams)
        print(f"The file '{contentpathteams}' has been successfully deleted.")
    else:
        print(f"The file '{contentpathteams}' does not exist.")

    
    #Liest den Wert in der Zelle in der ersten und zweiten Spalte der Excel Tabelle    
    print("teamsbefehl: ",teamsbefehl)
    
def deleteexcellineteams():
    #Liest die Excel-Datei erneut ein und löscht dann den Wert in der Zelle in der ersten Zeile und der zweiten Spalte.
    global teamsbefehl,contentpathteams
    #Read the Excel file
    data = pd.read_excel(contentpathteams)
    # Load the workbook
    workbook = openpyxl.load_workbook(contentpathteams)

    # Select the active worksheet
    sheet = workbook.active

    # Write to a single cell
    sheet['B2'] = "a"

    # Save the workbook
    workbook.save(contentpathteams)

#readexcelline()
#deleteexcelline()

    
#while(True):
    #readexcelline()
    #time.sleep(10)