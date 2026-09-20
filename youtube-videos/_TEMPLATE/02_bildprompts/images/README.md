# Kanonische Bilder

Dieser Ordner ist der technische Bilderordner für Phase 3.

Der Nutzer legt hier normalerweise **nicht manuell** Dateien ab. Stattdessen liegt die Google-Flow-ZIP unter:

```text
../bilder-zip/
```

Antigravity führt danach aus:

```bash
python tools/import_flow_zip.py \
  youtube-videos/THEMA/03_pipeline/scene-map.json \
  youtube-videos/THEMA/02_bildprompts/bilder-zip/bilder.zip \
  youtube-videos/THEMA/02_bildprompts/images
```

Danach enthält dieser Ordner exakt:

```text
Bild_01.png
Bild_02.png
Bild_03.png
...
```

Die Zuordnung erfolgt ausschließlich über die explizite Bildnummer im Dateinamen, niemals über die Reihenfolge innerhalb der ZIP.
