# Nutzer-Dateien-Standard

## Ziel

Alle Inhalte, die der Nutzer außerhalb des Repositories direkt öffnen und in eine andere KI oder Plattform kopieren soll, werden zusätzlich als normale `.txt`-Datei bereitgestellt.

Interne Agenten-/Technikdateien dürfen weiterhin `.md`, `.json`, `.py` usw. sein.

## Pflichtdateien pro YouTube-Video

### 1. Voiceover

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Inhalt: exakt derselbe gesprochene Text wie `01_script/script.txt`.

Zweck: in die Voice-KI kopieren.

### 2. Google Flow

```text
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Inhalt: der vollständige finale Google-Flow-Agent-Prompt inklusive aller Bildprompts.

Zweck: vollständig in Google Flow kopieren.

### 3. Antigravity

```text
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Inhalt: der vollständige finale Phase-3-Auftrag für Antigravity.

Zweck: bei Bedarf direkt in Antigravity kopieren.

### 4. YouTube

```text
04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Inhalt:

```text
TITEL
...

BESCHREIBUNG
...

HASHTAGS
...
```

Zweck: direkt in YouTube Studio kopieren.

## Synchronitätsregel

Die `.txt`-Dateien sind Nutzerkopien. Sie dürfen inhaltlich nicht von den jeweiligen kanonischen Projektdateien abweichen.

Beispiele:

```text
script.txt
= VOICEOVER-ZUM-KOPIEREN.txt

Google-Flow-Agent-Prompt.md
= GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt

Antigravity-Prompt.md
= ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt

YouTube-Caption.md
= YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Formatierungsunterschiede wie Markdown-Zeichen dürfen für bessere Kopierbarkeit entfernt werden, solange Inhalt und Anweisungen identisch bleiben.

## Regel für Phase 1

Phase 1 ist erst vollständig, wenn alle vier Nutzer-`.txt`-Dateien erzeugt und aktuell sind.

Der Nutzer soll für normale Kopieraufgaben **nicht** auf `.md`, `.json` oder interne Agentendateien angewiesen sein.

## Regel für zukünftige Dateien

Wenn später eine weitere Datei entsteht, deren Inhalt der Nutzer regelmäßig manuell in ein externes Tool kopieren muss, bekommt sie ebenfalls eine klar benannte `...-ZUM-KOPIEREN.txt`-Version.