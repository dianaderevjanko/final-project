# Izstrādes žurnāls - Izdevumu izsekotājs

## [2026-03-31] - 1. solis: Plānošana
- Definēta projekta arhitektūra un sadalījums 4 moduļos (`app`, `storage`, `logic`, `export`).
- Izveidots datu modelis JSON formātam.
- Inicializēts Git repozitorijs un izveidota mapju struktūra.
- *Izaicinājums:* Sākumā bija grūti izlemt, kuras funkcijas likt `logic.py` un kuras `app.py`. Nolēmu, ka `logic.py` būs tikai "tīra" matemātika bez `input/print`.

## [2026-04-01] - 2. solis: Pamata funkcionalitāte
- Izveidots `storage.py` modulis darbam ar JSON failu.
- Izveidotas pamatfunkcijas izdevumu pievienošanai un apskatei.
- **Problēmu risināšana:** Atklāju, ka lietotājs datuma vietā var ievadīt jebkādu tekstu (piem., "ēdiens 3eur"). 
- **Risinājums:** Ieviesu `is_valid_date` funkciju ar `datetime.strptime`, lai nodrošinātu datu integritāti.

## [2026-04-01] - 3. solis: Analītika un kārtošana
- Pievienota izdevumu filtrēšana pēc mēneša un kopsavilkums pa kategorijām.
- Ieviesta automātiskā datu kārtošana (sorting) pēc datuma hronoloģiskā secībā, izmantojot `lambda` funkciju.
- Pievienota izdevumu dzēšanas funkcija pēc kārtas numura.

## [2026-04-01] - 4. solis: Eksports un Bonusi
- Izveidots `export.py` modulis datu saglabāšanai CSV formātā.
- Izmantots `utf-8-sig` kodējums, lai nodrošinātu latviešu valodas simbolu pareizu attēlošanu Excel programmā.
- **Bonuss:** Pievienota meklēšanas funkcija pēc apraksta daļas.
- Pabeigta README.md dokumentācija ar lietošanas instrukciju.