# DLBDSEDE02 - Projekt: Data Analysis
Dieses Repository enthält den Source-Code, welche ich für die Umsetzung dieses Projekts verwendet habe. Die Rohdaten, welche in diesem Projekt verarbeitet werden, werden automatisch heruntergeladen. Im Ordner `data` ist ein Sample vom [21.10.2023](data/2023-10-21.json) enthalten (für den Fall das die API Änderungen erfährt oder offline ist).

## Voraussetzungen
Ich habe die Arbeit in einem Jupyter Notebook entwickelt (siehe [hier](src/aufgabe1.ipynb)), basierend auf einer Standard-Installation von Anaconda. Da ich persönlich die DX (Developer Experience) von Jupyter Notebooks als nicht ausreichend empfinde, habe ich die Implementierung mit [Visual Studio Code](https://code.visualstudio.com/) vorgenommen.

### Variante 1: Lokale Installation
Zur lokalen installation muss [Anaconda 3 2023.9.0](https://www.anaconda.com/download) installiert sein.

Alle verwendeten Visual Studio Code Erweiterungen sollten beim ersten öffnen des Ordners direkt zur Installation vorgeschlagen werden. Die notwendigen Python-Pakete werden innerhalb des Notebooks installiert, deswegen ist keine weitere Vorbereitung nötig.

### Variante 2: Dev Containers
Falls keine lokale Anaconda-Installation vorhanden ist, kann die ganze Laufzeitumgebung auch als Docker Container in einem DevContainer gestartet werden. Dazu muss lediglich die VS Code Erweiterung [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installiert werden, das IDE sollte nun den konfigurierten Container automatisch erkennen.

Dieser Container enthält auch alle empfohlenen VS Code Erweiterungen und alle für das Notebook nötigen Pakete.

## Notebook ausführen
Das Notebook kann ohne weitere Konfigurationen ausgeführt werden. Die detaillierten Beschreibungen für die Einzelschritte sind direkt im Notebook als Markdown-Zellen hinterlegt.

Falls gewünscht, kann auch das verwendete Profil in Code importiert und verwendet werden, es ist unter [tools/data-science.code-profile](tools/data-science.code-profile) zu finden.