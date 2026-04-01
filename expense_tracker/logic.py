#Programmas loģika

from datetime import datetime

def sum_total(expenses):
    """
    Aprēķina visu izdevumu kopējo summu.
    Parametri: expenses (list) - saraksts ar vārdnīcām
    Atgriež: float - kopsumma
    """
    # sum() saskaita visas 'amount' vērtības no saraksta
    return sum(expense["amount"] for expense in expenses)

def filter_by_month(expenses, year, month):
    """
    Atgriež tikai norādītā mēneša izdevumus.
    """
    result = []
    for expense in expenses:
        # Pārvēršam teksta datumu "2025-02-15" par Python datuma objektu
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        
        # Pārbaudām, vai gads un mēnesis sakrīt ar meklēto
        if d.year == year and d.month == month:
            result.append(expense)
            
    return result

def sum_by_category(expenses):
    """
    Saskaita, cik kopā iztērēts katrā kategorijā.
    Atgriež vārdnīcu: {"Ēdiens": 25.50, "Transports": 10.00, ...}
    """
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        amount = expense["amount"]
        # Ja kategorija vēl nav vārdnīcā, sākam ar 0 un pieskaitām summu
        totals[cat] = totals.get(cat, 0) + amount
        
    # Noapaļojam rezultātus līdz 2 zīmēm aiz komata
    return {cat: round(val, 2) for cat, val in totals.items()}

def get_available_months(expenses):
    """
    Atrod visus unikālos mēnešus (piem., "2025-01", "2025-02"), kuros ir bijuši tēriņi.
    """
    months = set() # Set automātiski neļauj dublikātus
    for expense in expenses:
        # Paņemam pirmos 7 simbolus no datuma "2025-02-15" -> "2025-02"
        months.add(expense["date"][:7])
    return sorted(list(months)) # Atgriežam sakārtotu sarakstu

def sort_expenses_by_date(expenses):
    """
    Sakārto izdevumus hronoloģiskā secībā pēc datuma.
    """
    # Izmantojam Python iebūvēto sorted() funkciju. 
    # 'key' pasaka datoram, ka jāskatās tieši uz "date" lauku.
    return sorted(expenses, key=lambda x: x["date"])