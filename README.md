# Kodi German Streaming Addon

Ein umfassendes Kodi-Addon für deutsche Streaming-Dienste mit nativer App-Integration für Android.

## Features

- 🎬 Integration aller großen deutschen Streaming-Anbieter
- 🎯 Schnelle Navigation zwischen Diensten
- 📱 Native Android App-Integration
- 🔍 Suchfunktion für Filme und Serien
- 🎨 Benutzerfreundliche Oberfläche ähnlich Plex
- 📲 Optimiert für Android-Geräte

## Unterstützte Streaming-Dienste

- **Netflix** - Filme, Serien und Dokumentationen
- **Amazon Prime Video** - Filme, Serien und Originales
- **Disney+** - Disney, Pixar, Marvel und Star Wars
- **Sky** - Filme, Serien und Live-TV
- **DAZN** - Sport Live und On-Demand
- **RTL+** - RTL Serien, Filme und Shows
- **Joyn (ProSieben)** - ProSieben, Sat.1 und Kabel Eins
- **MagentaTV** - Deutsche Telekom Streaming-Dienst
- **MUBI** - Kino Klassiker und Independent Filme
- **YouTube** - Videos und Kanäle

## Installation

### Voraussetzungen
- Kodi 19+ auf Android
- Python 3.6+
- Internetverbindung
- Streaming-Apps installiert

### Installation von GitHub

1. Lade das Repository herunter oder klone es:
   ```bash
   git clone https://github.com/Thgit20/kodi-german-streaming-addon.git
   ```

2. Kopiere das Addon-Verzeichnis in dein Kodi Addons-Verzeichnis:
   ```
   ~/.kodi/addons/plugin.video.german.streaming/
   ```
   oder auf Android:
   ```
   /storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/addons/
   ```

3. Starte Kodi neu

4. Gehe zu Addons → Video-Addons → German Streaming

## Verwendung

1. **Öffne das Addon** über Addons → Video-Addons → German Streaming
2. **Wähle einen Streaming-Dienst** aus der Liste
3. **Öffne die native App** oder nutze die Suchfunktion
4. Filme und Serien werden direkt in der jeweiligen Streaming-App geladen

## Struktur

```
kodi-german-streaming-addon/
├── addon.xml           # Addon-Konfiguration
├── default.py          # Hauptskript
├── icon.png            # Addon-Icon
├── fanart.jpg          # Hintergrund
├── screenshot.jpg      # Screenshot
├── resources/
│   ├── settings.xml    # Einstellungen
│   └── strings.json    # Sprachdateien
└── README.md           # Dokumentation
```

## Konfiguration

### Einstellungen anpassen

Hinweis: Diese können später über die Addon-Einstellungen in Kodi angepasst werden:

- Standard-Streaming-Dienst
- Video-Qualität
- Sprache
- Auto-Play-Funktion

## Troubleshooting

### App öffnet sich nicht
- Stelle sicher, dass die Streaming-App auf deinem Android-Gerät installiert ist
- Überprüfe die Paketname in `default.py`
- Schau in die Kodi-Logs für Fehler: `~/.kodi/temp/kodi.log`

### Addon wird nicht angezeigt
- Kodi neu starten
- Addon neu installieren
- Stelle sicher, dass Python 3.6+ installiert ist

## Entwicklung

### Neue Streaming-Dienste hinzufügen

Öffne `default.py` und füge in der `STREAMING_SERVICES` Dictionary einen neuen Eintrag hinzu:

```python
'service_id': {
    'name': 'Service Name',
    'package': 'com.package.name',
    'icon': 'https://icon-url.com/icon.png',
    'description': 'Beschreibung'
}
```

## Lizenz

GPL-3.0 License

## Kontakt & Support

- Issues: https://github.com/Thgit20/kodi-german-streaming-addon/issues
- Diskussionen: https://github.com/Thgit20/kodi-german-streaming-addon/discussions

## Disclaimer

Dieses Addon ist nicht offiziell mit den Streaming-Diensten verbunden. Es ist nur ein Tool zur einfacheren Navigation zwischen den Diensten. Du brauchst valid Abos bei den jeweiligen Anbietern.

## Changelog

### Version 1.0.0 (Initial Release)
- Erste Veröffentlichung
- Unterstützung für 10 deutsche Streaming-Dienste
- Native App-Integration
- Suchfunktion