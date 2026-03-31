#Datu slānis - programmas "noliktavas pārzinis". Viņš neinteresējas par to, kas ir nopirkts, viņš tikai māk datus nolikt "plauktā" (failā) un paņemt no tā.

import json
import os

# Faila nosaukums, kurā glabāsim visus datus
FILENAME = "expenses.json"

def load_expenses():
    """
    Nolasa izdevumu sarakstu no JSON faila. 
    Ja fails neeksistē, atgriež tukšu sarakstu [].
    """
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, "r", encoding="utf-8") as f:
        # json.load pārvērš JSON tekstu atpakaļ par Python sarakstu
        return json.load(f)

def save_expenses(expenses):
    """
    Saglabā izdevumu sarakstu JSON failā.
    """
    with open(FILENAME, "w", encoding="utf-8") as f:
        # ensure_ascii=False ļauj failā redzēt latviešu burtus (ā, ē, š...)
        # indent=2 padara failu glītu un lasāmu cilvēkam
        json.dump(expenses, f, indent=2, ensure_ascii=False)