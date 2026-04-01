#Galvenā programma

import sys
from datetime import date
import storage
import logic
from export import export_to_csv

# Definējam atļautās kategorijas
CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Māja", "Veselība", "Iepirkšanās", "Cits"]

from datetime import datetime

def is_valid_date(text):
    """Pārbauda, vai teksts ir derīgs datums YYYY-MM-DD formātā."""
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def add_expense(expenses):
    """Lietotāja ievade jaunam izdevumam."""
    print("\n--- Pievienot izdevumu ---")
    
    # 1. Datums (automātiski piedāvā šodienu)
    while True:
        today = date.today().strftime("%Y-%m-%d")
        datums = input(f"Datums (YYYY-MM-DD) [{today}]: ") or today
        
        if is_valid_date(datums):
            break
        else:
            print("❌ Nepareizs formāts! Lūdzu, izmanto GGGG-MM-DD (piem., 2026-03-31)")
    
    # 2. Kategorijas izvēle
    print("Kategorijas:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")
    
    try:
        izvele = int(input(f"Izvēlies (1-{len(CATEGORIES)}): "))
        kategorija = CATEGORIES[izvele - 1]
    except (ValueError, IndexError):
        print("❌ Nepareiza izvēle, izmantosim 'Cits'")
        kategorija = "Cits"

    # 3. Summa (ar mūsu viltību pret komatiem)
    try:
        summa_str = input("Summa (EUR): ").replace(',', '.')
        summa = float(summa_str)
        if summa <= 0: raise ValueError
    except ValueError:
        print("❌ Nepareiza summa. Izdevums netika pievienots.")
        return

    # 4. Apraksts
    apraksts = input("Apraksts: ")

    # Pievienojam sarakstam un saglabājam
    jauns_izdevums = {
        "date": datums,
        "amount": summa,
        "category": kategorija,
        "description": apraksts
    }
    expenses.append(jauns_izdevums)
    storage.save_expenses(expenses)
    print(f"✓ Pievienots: {datums} | {kategorija} | {summa:.2f} EUR")

def list_expenses(expenses):
    """Parāda visus izdevumus glītā tabulā."""
    if not expenses:
        print("\nSaraksts ir tukšs.")
        return
    
    # Sakārtojam datus pirms rādīšanas
    expenses = logic.sort_expenses_by_date(expenses)

    print(f"\n{'Datums':<12} {'Summa':>10} {'Kategorija':<15} {'Apraksts'}")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp['date']:<12} {exp['amount']:>8.2f} EUR {exp['category']:<15} {exp['description']}")
    
    kopsumma = logic.sum_total(expenses)
    print("-" * 60)
    print(f"KOPĀ: {kopsumma:.2f} EUR ({len(expenses)} ieraksti)")

def main():
    expenses = storage.load_expenses()
    
    while True:
        print("\n=== IZDEVUMU IZSEKOTĀJS ===")
        print("1) Pievienot izdevumu")
        print("2) Parādīt visus izdevumus")
        print("3) Filtrēt pēc mēneša")     
        print("4) Kopsavilkums pa kategorijām") 
        print("5) Dzēst izdevumu")         
        print("6) Eksportēt uz CSV")  
        print("7) Meklēt izdevumus")
        print("8) Iziet")
        
        izvele = input("\nIzvēlies darbību (1-8): ")
        
        if izvele == "1":
            add_expense(expenses)
        elif izvele == "2":
            list_expenses(expenses)
        elif izvele == "3":               
            filter_menu(expenses)
        elif izvele == "4":               
            show_category_summary(expenses)
        elif izvele == "5":               
            delete_expense(expenses)
        elif izvele == "6":               
            export_menu(expenses)
        elif izvele == "7":
            search_menu(expenses)
        elif izvele == "8":
            print("Uz redzēšanos!")
            break
        else:
            print("❌ Nepareiza izvēle, mēģini vēlreiz.")

def show_category_summary(expenses):
    """Parāda kopsavilkumu pa kategorijām."""
    if not expenses:
        print("\nSaraksts ir tukšs.")
        return

    print("\n--- KOPSAVILKUMS PA KATEGORIJĀM ---")
    summary = logic.sum_by_category(expenses)
    
    for cat, total in summary.items():
        print(f"  {cat:<20} {total:>8.2f} EUR")
    
    print("-" * 30)
    print(f"  {'KOPĀ:':<20} {logic.sum_total(expenses):>8.2f} EUR")

def filter_menu(expenses):
    """Lietotājs izvēlas mēnesi un redz filtrētu sarakstu."""
    months = logic.get_available_months(expenses)
    
    if not months:
        print("\nNav datu, ko filtrēt.")
        return

    print("\nPieejamie mēneši:")
    for i, m in enumerate(months, 1):
        print(f"  {i}) {m}")
    
    try:
        izvele = int(input(f"Izvēlies mēnesi (1-{len(months)}): "))
        selected_month_str = months[izvele - 1] # Piemēram "2025-03"
        
        # Sadalām "2025-03" uz gadu (2025) un mēnesi (3)
        year = int(selected_month_str[:4])
        month = int(selected_month_str[5:])
        
        filtered = logic.filter_by_month(expenses, year, month)
        
        print(f"\n--- IZDEVUMI PAR {selected_month_str} ---")
        list_expenses(filtered) # Izmantojam jau esošo tabulas funkciju
        
    except (ValueError, IndexError):
        print("❌ Nepareiza izvēle.")

def delete_expense(expenses):
    """Ļauj lietotājam izdzēst izdevumu pēc tā kārtas numura."""
    if not expenses:
        print("\nNav ko dzēst.")
        return

    # Sākumā parādām sarakstu, lai lietotājs redz numurus
    print("\n--- DZĒST IZDEVUMU ---")
    # Šeit svarīgi: mēs parādām sakārtotu sarakstu!
    sorted_expenses = logic.sort_expenses_by_date(expenses)
    
    for i, exp in enumerate(sorted_expenses, 1):
        print(f"{i}) {exp['date']} | {exp['amount']} EUR | {exp['description']}")

    try:
        izvele = int(input("\nIevadi numuru, kuru dzēst (vai 0, lai atceltu): "))
        if izvele == 0: return
        
        # Izdzēšam izvēlēto elementu no saraksta
        deleted = sorted_expenses.pop(izvele - 1)
        
        # Tā kā mēs izdzēsām no sakārtotā saraksta, mums jāsaglabā viss saraksts
        storage.save_expenses(sorted_expenses)
        print(f"✓ Izdzēsts: {deleted['description']}")
        
    except (ValueError, IndexError):
        print("❌ Nepareizs numurs!")

def export_menu(expenses):
    """Prasa lietotājam faila nosaukumu un eksportē datus."""
    if not expenses:
        print("\nNav datu, ko eksportēt.")
        return

    vards = input("\nIevadi faila nosaukumu (piem., tēriņi.csv) [izdevumi.csv]: ") or "izdevumi.csv"
    
    # Ja nosaukumā nav .csv, pieliekam to
    if not vards.endswith(".csv"):
        vards += ".csv"
        
    if export_to_csv(expenses, vards):
        print(f"✓ Eksportēts: {len(expenses)} ieraksti -> {vards}")

def search_menu(expenses):
    query = input("\nIevadi meklējamo vārdu (piem., 'kafija'): ")
    found = logic.search_expenses(expenses, query)
    
    print(f"\n--- MEKLĒŠANAS REZULTĀTI: '{query}' ---")
    list_expenses(found) # izmantojam savu gatavo tabulas funkciju!

if __name__ == "__main__":
    main()