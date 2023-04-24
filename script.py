# Datenkonventierer, um Dateien von JSON zu CSV und umgekehrt zu schreiben.
# Für mehr Infos die "5" in das Programm eingeben

# Erstellt von Mike, Marco und Dogus
# Zuletzt bearbeitet am 19.11.2021
# Version 7


# benötigte Module importieren
import sys
import os
import csv
import json
import time

#Endlosschleife
while 1:
    # Programmüberschrift
    print("---------------------")
    print("CSV-JSON-Konvertierer")
    print("---------------------")
    # Menü und Benutzerauswahl
    print("(1) CSV-Datei anzeigen")
    print("(2) JSON-Datei anzeigen")
    print("(3) CSV -> JSON")
    print("(4) JSON -> CSV")
    print("(5) READ-ME")
    print("(0) Ende")
    print("")
    befehl = int(input("Menüauswahl 0-5 : "))

    # Testen, ob ein bekannter Befehl eingegeben wurde
    if(befehl != 0 and befehl != 1 and befehl != 2 and befehl != 3 and befehl != 4 and befehl !=5):
        print("Unbekannter Befehl: " + str(befehl))
        continue


    #Eingabe der Dateiinformationen
    #Konvertierer beenden
    if befehl == 0:
        print("Konvertierer beendet")
        break
    
    # Name der zu auslesenden Datei   
    if befehl == 1:
        nameEingabeDatei = input("Pfad + Name auszulesenden CSV-Datei: ")
    if befehl == 2:
        nameEingabeDatei = input("Pfad + Name auszulesenden JSON-Datei: ")

        
    #Name der JSON-Ausgabedatei bei konvertierung mit automatischer Dateiendung
    if befehl == 3:
        nameEingabeDatei = input("Pfad + Name der CSV-Eingabedatei: ")
        nameAusgabeDatei = input("Name der JSON-Ausgabedatei: ") + ".json"

        # Testen, ob Eingabedatei existiert
        if os.path.isfile(nameEingabeDatei) != True:
            print("")
            print("FEHLER:")
            print("Eingabedatei: " + nameEingabeDatei + " nicht gefunden!")
            print("")
            print("Programm wird neu gestartet...")
            print("")
            print("")
            continue

        
    #Name der CSV-Ausgabedatei bei konvertierung mit automatischer Dateiendung
    if befehl == 4:
        nameEingabeDatei = input("Pfad + Name der JSON-Eingabedatei: ")
        nameAusgabeDatei = input("Name der CSV-Ausgabedatei: ") + ".csv"

        # Testen, ob Eingabedatei existiert
        if os.path.isfile(nameEingabeDatei) != True:
            print("")
            print("FEHLER:")
            print("Eingabedatei: " + nameEingabeDatei + " nicht gefunden!")
            print("")
            print("Programm wird neu gestartet...")
            print("")
            print("")
            continue



    #Ausführung der Menüoptionen
    #CSV-Datei auslesen   
    if befehl == 1:
        print("Eingabedatei einlesen ...")
        results = open(nameEingabeDatei, "r", encoding="utf-8")
        csv_reader_object = csv.reader(results, delimiter=',')
        #Zählen der Datensätze
        i = 0
        for row in csv_reader_object:
            print(row)
            i = i + 1
        print("Anzahl der ausgelesenen Datensätze: ",i)


    #JSON-Datei auslesen   
    if befehl == 2:
        with open(nameEingabeDatei, 'r') as json_file:
            json_data = json.load(json_file)
            print(json_data)
            #Zählen der Datensätze
            i = 0
            with open(nameEingabeDatei) as f:
                for line in f:
                    i = i + 1
            print("Anzahl der ausgelesenen Datensätze: ",i)


    #Umwandlung: CSV -> JSON
    if befehl == 3:
        #Zeitmessungsbeginn
        zeit_start = time.time()
        print("")
        print("Eingabedatei einlesen ...")
        # CSV-Datei öffnen
        csvdatei = open(nameEingabeDatei, "r", encoding="utf-8")
        reader = csv.DictReader(csvdatei, fieldnames=None)
        # Umwandeln
        print("")
        print("In JSON-Format verwandeln ...")
        out = json.dumps([row for row in reader], indent=4, ensure_ascii=False)
        print("")
        print("JSON-Datei erstellen ...")
        # JSON-Datei rausschreiben
        jsonDatei = open(nameAusgabeDatei, "w", encoding="utf-8")
        jsonDatei.write(out)
        jsonDatei.close()
        #Ausgabe der Programmnachrichten
        print("")
        print("Konvertierung: CSV -> JSON")
        print("")
        print("Ausgabedatei: " + nameAusgabeDatei + " erfolgreich erstellt.")
        print("")
        #Zählen der Datensätze
        i = 0
        with open(nameEingabeDatei) as f:
                for line in f:
                    i = i + 1
        print("Anzahl der umgewandelten Datensätze: ",i)
        #Zeitmessungsende + Zeitumrechnung + Zeitausgabe
        zeit_stop = time.time()
        zeit = zeit_stop - zeit_start
        zeit = str(round(zeit, 2))
        print("Umwandlungsdauer:",zeit,"Sekunden")
        

    #Umwandlung: JSON -> CSV
    if befehl == 4:
        zeit_start = time.time()
        print("")
        print("Eingabedatei einlesen ...")
        with open(nameEingabeDatei) as json_file:
            jsondata = json.load(json_file)
            data_file = open(nameAusgabeDatei, 'w', newline='')
            csv_writer = csv.writer(data_file)
            #Zählen der Datensätze
            count = 0
        for data in jsondata:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count = count + 1
            csv_writer.writerow(data.values())
        #Ausgabe der Programmnachrichten
        print("")
        print("Konvertierung: JSON -> CSV")
        print("")
        print("Ausgabedatei: " + nameAusgabeDatei + " erfolgreich erstellt.")
        print("")
        data_file.close()
        #Zählen der Datensätze
        i = 0
        with open(nameEingabeDatei) as f:
            for line in f:
                i = i + 1
        print("Anzahl der umgewandelten Datensätze: ",i)
        #Zeitmessungsende + Zeitumrechnung + Zeitausgabe
        zeit_stop = time.time()
        zeit = zeit_stop - zeit_start
        zeit = str(round(zeit, 2))
        print("Umwandlungsdauer:",zeit,"Sekunden")

        
    #READ-ME zum besseren Verständnis
    if befehl == 5:
        print("")
        print("[-----------------------------------------------------------]")
        print("[---------------------- R E A D   M E ----------------------]")
        print("[-----------------------------------------------------------]")
        print("")
        print("Das Programm dient der Umwandlung von CSV und JSON Dateien.")
        print("Diese Dateien können ebenfalls angezeigt werden.")
        print("")
        print("Bei der Dateieingabe muss der Pfad der Datei mit eingegeben")
        print("werden, sowie der Dateityp.")
        print("Beispiel: Datei.csv / Nicht: Datei")
        print("Wenn eine Datei nicht eingelesen werden kann, wird das")
        print("Programm neu gestartet")
        print("")
        print("Bei der Dateiausgabe reicht der Name, die die Datei haben")
        print("soll.")
        print("Eine Dateiendung wird NICHT benötigt (wie .json).")
        print("")
        print("Die Ausgabedatei wird in dem selben Verzeichnis gespeichert,")
        print("wie dieses Programm.")
        print("")
        print("[-----------------------------------------------------------]")
        print("[-----------------------------------------------------------]")
        print("[-----------------------------------------------------------]")
        print("")


    # Leerzeile für die Optik
    print("")

sys.exit(0)
