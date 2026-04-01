#Eksports uz Excel

import csv

def export_to_csv(expenses, filepath):
    """
    Eksportē izdevumus CSV failā, ko var atvērt Excel.
    """
    try:
        # utf-8-sig ir triks, lai Excel saprastu latviešu burtus (ā, ē, š...)
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            
            # Ierakstām virsrakstu rindu
            writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
            
            # Ierakstām visus datus
            for exp in expenses:
                writer.writerow([
                    exp["date"],
                    f"{exp['amount']:.2f}",
                    exp["category"],
                    exp["description"]
                ])
        return True
    except Exception as e:
        print(f"❌ Kļūda eksportējot: {e}")
        return False