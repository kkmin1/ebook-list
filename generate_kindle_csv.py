import csv

kindle_books = [
    {"App": "Kindle", "Title": "Heat_Wave_Equation"},
    {"App": "Kindle", "Title": "라그랑주 역학과 스라파 경제학"},
    {"App": "Kindle", "Title": "고전역학"},
    {"App": "Kindle", "Title": "Tirole의 시장규제 이론"},
    {"App": "Kindle", "Title": "statphys"},
    {"App": "Kindle", "Title": "profoundphysics com lagrangian mechanics for beginners"},
    {"App": "Kindle", "Title": "Physics"},
    {"App": "Kindle", "Title": "intro_physics_1"},
    {"App": "Kindle", "Title": "Why Stock Markets Crash: 49 (Princeton Science Library)"},
    {"App": "Kindle", "Title": "A Criticism of Modern Micro-founded Macroeconomics"},
    {"App": "Kindle", "Title": "cmech"},
    {"App": "Kindle", "Title": "Classical Dynamics"},
    {"App": "Kindle", "Title": "calcus"},
    {"App": "Kindle", "Title": "Game Theory"},
    {"App": "Kindle", "Title": "The Misbehavior of Markets: A Fractal View of Financial Turbulence"},
    {"App": "Kindle", "Title": "Inflation"},
    {"App": "Kindle", "Title": "Safe Area Gorazde: The War in Eastern Bosnia 1992-1995"},
    {"App": "Kindle", "Title": "The Road to Reality"},
    {"App": "Kindle", "Title": "The Black Swan: Second Edition: The Impact of the Highly Improbable"}
]

filename = r"c:\Users\kkmin\Desktop\ebook\kindle_ebook_list.csv"
with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=["App", "Title"])
    writer.writeheader()
    writer.writerows(kindle_books)

print(f"File created: {filename}")
