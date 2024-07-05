import cv2
#Importiert CV2 für die Bildverarbeitung
import os
#Wird Importiert für die Interaktion mit Dateisystem
from moviepy.editor import VideoFileClip
#Wird Impotiert um Videos zu bearbeiten
import pyautogui
#Wird Importiert für die Automatisierung von Maus- und Tastatureingaben
import time
#Wird Impotiert zur Handhabung von Zeitintervallen

def get_video_duration(video_path):
    #Lädt ein Video und gibt die Dauer des Videos in Sekunden zurück
    try:
        clip = VideoFileClip(video_path)
        duration = round(clip.duration)
        clip.close()
        return duration
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def check_file_exists(file_path):
    #Überprüfen, ob die Datei existiert
    if not os.path.exists(file_path):
        print(f"Die Datei {file_path} konnte nicht gefunden werden. Bitte überprüfen Sie den Pfad.")
        return False
    return True

def image_to_video(image_path, video_path, duration=5):
    #Überprüfen, ob das Bild existiert
    if not check_file_exists(image_path):
        return

    # Bild laden
    frame = cv2.imread(image_path)
    
    #Überprüfen, ob das Bild korrekt geladen wurde
    if frame is None:
        print("Fehler beim Laden des Bildes. Bitte überprüfen Sie das Dateiformat und den Pfad.")
        return
    
    #Höhe und Breite des Bildes bestimmen
    height, width, layers = frame.shape

    #Video Writer initialisieren
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'DIVX'), 1, (width, height))

    #Das Bild für die Dauer des Videos einfügen
    for _ in range(duration):
        video.write(frame)

    #Video Writer schliessen
    video.release()
    print("Video erfolgreich erstellt und gespeichert.")

def play_video(video_path):
    #Überprüfen, ob das Video existiert
    if not check_file_exists(video_path):
        return
    seconds = get_video_duration(video_path)
    seconds -= 2
    #Verwenden Sie os.system, um den Windows Media Player zu öffnen
    os.system(f"start wmplayer {video_path}")
    time.sleep(2)
    pyautogui.hotkey('alt', 'enter')
    os.system(f"timeout {seconds} && taskkill /im wmplayer.exe /f")
    print("Video wird abgespielt.")
    print(seconds)

# Bildpfad und Videopfad definieren
#image_path = r"C:\Temp\20770858-hd_1080_1920_30fps.mp4"  # Pfad zum Bild anpassen, als Raw-String
#video_path = r'C:\Temp\20770858-hd_1080_1920_30fps.mp4'  # Pfad zum Ausgabevideo, als Raw-String

# Bild zu Video konvertieren
#image_to_video(image_path, video_path)

# Video abspielen
#play_video(video_path)
