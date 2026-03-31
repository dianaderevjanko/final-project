"Izdevumu izsekotājs ir programma, kas palīdz cilvēkiem kontrolēt savas finanses. 
Tā ļauj pierakstīt katru pirkumu, redzēt mēneša kopsavilkumu un beigās sagatavot Excel failu (CSV) analīzei."

Datu struktūra:
    Datumu filtrēšanai, summu rēķināšanai un kategoriju, lai zinātu, kur nauda "aiziet"

  "date": "2026-03-31",
  "amount": 15.50,
  "category": "Ēdiens",
  "description": "Pusdienas darbā"

Moduļu plāns:
1. ''storage.py: Tikai darbam ar JSON failu (glabātuve).
2. logic.py: Tikai matemātikai un filtrēšanai (smadzenes).
3. export.py: Tikai CSV faila veidošanai (eksports).
4. app.py: Saruna ar lietotāju un izvēlne (seja).''

Lietotāja scenāriji:
    Piemērs: "Lietotājs mēģina ievadīt summu 'desmit'. Programma saprot, ka tas nav skaitlis, un laipni lūdz ievadīt 10.00."