#Galvenā programma

import sys
from datetime import date
import storage
import logic

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
        print("7) Iziet")
        
        izvele = input("\nIzvēlies darbību (1-7): ")
        
        if izvele == "1":
            add_expense(expenses)
        elif izvele == "2":
            list_expenses(expenses)
        elif izvele == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("❌ Nepareiza izvēle, mēģini vēlreiz.")

if __name__ == "__main__":
    main()