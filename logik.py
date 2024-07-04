import pandas as pd
#Pandas Bibliothek wird Importiert um Daten aus Excel Dateien lesen zu können
import cv2
#Importiert die OpenCV-Bibliothek für die Videoverarbeitung
import os
#Importiert das Betriebssystem-interaktive Modul in Python
import time
#Importiert das Zeitmodul
import csv
#Importiert das CSV-Modul, das das Lesen und Schreiben von CSV-Dateien ermöglicht
import DataIO, BildaufWindowsMediaPlayeranzeigen,Changetracking
#Importiert die Skripte DataIO und BildaufWindowsMediaPlayer


def main():
    logik2()
#Ruft Argumente im Logik 2 auf
def logik2():
    is_modified = Changetracking.check_file_modified(DataIO.contentpathteams)
    print("File has been modified:", is_modified)
    DataIO.readexcellineteams()
    if  is_modified == True: 
        
        print("teamsbefehl: ",DataIO.teamsbefehl )
        #Überprüft ob die DataIO.Teamsbefehl nicht leer ist
        DataIO.readexcellinedata()
        #Wenn Befehl nicht leer dann wird die Funkton aus dem Modul aufgerufen
        contentpfad = DataIO.teamsbefehlzeile.iloc[0, 1]
        #Der Inhalt wird der contenpfad Variabeln zugewiesen
        BildaufWindowsMediaPlayeranzeigen.play_video(contentpfad)
       #DataIO.deleteexcellineteams()
        #Die Funktion wird mit dem contentpfad aufgerufen
       
if __name__ == "__main__":
    while(True):
        main()
        #time.sleep(1)
    #Dieser Teil des Codes prüft, ob das Skript direkt ausgeführt wird, und wenn ja, wird die main-Funktion aufgerufen.