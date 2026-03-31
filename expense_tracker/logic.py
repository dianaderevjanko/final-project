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