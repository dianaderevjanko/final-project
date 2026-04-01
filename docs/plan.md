# Projekta plāns: Izdevumu izsekotājs

## A. Programmas apraksts
Izdevumu izsekotājs ir programma, kas palīdz cilvēkiem kontrolēt savas finanses. Tā ļauj pierakstīt katru pirkumu, redzēt mēneša kopsavilkumu un beigās sagatavot Excel failu (CSV) analīzei.

## B. Datu struktūra
Ieraksts tiek glabāts kā vārdnīca, lai nodrošinātu datumu filtrēšanu, summu rēķināšanu un kategoriju analīzi.
Piemērs:
{
  "date": "2026-03-31",
  "amount": 15.50,
  "category": "Ēdiens",
  "description": "Pusdienas darbā"
}

## C. Moduļu plāns
1. **storage.py**: Tikai darbam ar JSON failu (glabātuve).
2. **logic.py**: Tikai matemātikai un filtrēšanai (smadzenes).
3. **export.py**: Tikai CSV faila veidošanai (eksports).
4. **app.py**: Saruna ar lietotāju un izvēlne (seja).

## D. Lietotāja scenāriji
- **Pievienošana:** Lietotājs mēģina ievadīt summu 'desmit'. Programma saprot, ka tas nav skaitlis, un laipni lūdz ievadīt 10.00.
- **Analīze:** Lietotājs izvēlas apskatīt marta izdevumus. Programma filtrē sarakstu un parāda tikai attiecīgā mēneša tēriņus un kopsummu.

## E. Robežgadījumi
- Ja fails `expenses.json` neeksistē, programma automātiski izveido tukšu sarakstu.
- Ja lietotājs ievada nepareizu datuma formātu, programma pieprasa ievadi atkārtot hronoloģiskā formātā (YYYY-MM-DD).