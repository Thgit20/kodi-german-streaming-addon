# Kodi German Streaming Addon - ZIP Distribution

Für die einfache Installation in Kodi ohne Repository kannst du die ZIP-Datei direkt verwenden.

## Download

Die ZIP-Dateien findest du unter:
**Releases:** https://github.com/Thgit20/kodi-german-streaming-addon/releases

## Installation in Kodi

### Schritt 1: ZIP-Datei herunterladen
1. Gehe zu: https://github.com/Thgit20/kodi-german-streaming-addon/releases
2. Lade die neueste `plugin.video.german.streaming-*.zip` Datei herunter

### Schritt 2: In Kodi installieren
1. Öffne **Kodi**
2. Gehe zu: **Add-ons → Addon Manager → Aus ZIP-Datei installieren**
3. Navigiere zur heruntergeladenen ZIP-Datei
4. Wähle `plugin.video.german.streaming-*.zip`
5. Klicke OK und warte auf die Installation

### Schritt 3: Addon starten
1. Gehe zu: **Add-ons → Video-Addons**
2. Klick auf **German Streaming**
3. Genießen! 🎬

## Inhaltsverzeichnis der ZIP

```
plugin.video.german.streaming-1.0.0.zip
└── plugin.video.german.streaming/
    ├── addon.xml                 # Addon-Konfiguration
    ├── default.py                # Hauptscript
    ├── icon.png                  # Addon-Icon
    ├── fanart.jpg                # Hinterground
    ├── screenshot.jpg            # Screenshot
    └── resources/
        ├── settings.xml          # Einstellungen
        └── strings.json          # Sprachdateien
```

## Troubleshooting

### ZIP kann nicht installiert werden
- Stelle sicher, dass die ZIP-Datei vollständig heruntergeladen ist
- Überprüfe den Dateinamen (sollte mit `.zip` enden)
- Kodi neu starten und erneut versuchen

### Addon wird nach Installation nicht angezeigt
- Gehe zu: **Einstellungen → System → Add-ons**
- Stelle sicher, dass "Unbekannte Quellen" aktiviert ist
- Kodi neu starten

### Addon-Fehler beim Starten
- Schau in die Kodi-Logs: `~/.kodi/temp/kodi.log`
- Stelle sicher, dass Python 3.6+ installiert ist
- Überprüfe, dass deine Streaming-Apps installiert sind

## ZIP manuell erstellen

Falls du die ZIP selbst erstellen möchtest:

### Option 1: Mit dem bereitgestellten Script (Linux/Mac)
```bash
bash create_zip.sh
```

### Option 2: Manuell
1. Kopiere den Ordner `plugin.video.german.streaming` (mit allen Dateien)
2. Packe ihn als ZIP: `plugin.video.german.streaming-1.0.0.zip`
3. Fertig!

## Updatews mit ZIP

Falls du ein Update durchführen möchtest:
1. Deinstalliere das alte Addon: **Add-ons → German Streaming → Deinstallieren**
2. Lade die neue ZIP herunter
3. Installiere die neue ZIP wie oben beschrieben

## Support

Bei Problemen:
- Issues: https://github.com/Thgit20/kodi-german-streaming-addon/issues
- Diskussionen: https://github.com/Thgit20/kodi-german-streaming-addon/discussions
