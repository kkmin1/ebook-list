import csv

csv_path = r"C:\Users\kkmin\Desktop\ebook\ridibooks_extracted_list.csv"
cleaned_list = []

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row['Title']
        title = title.replace(" e북는 리디", "")
        title = title.replace(" - 판타지 웹소설", "")
        row['Title'] = title
        cleaned_list.append(row)

with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=["App", "FolderID", "Title"])
    writer.writeheader()
    writer.writerows(cleaned_list)

print("Title names cleaned.")

existing_list_path = r"c:\Users\kkmin\Desktop\ebook\ebook_list.csv"
existing_list = []
try:
    with open(existing_list_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_list.append(row)
except:
    pass

for item in cleaned_list:
    existing_list.append({"App": item["App"], "Title": item["Title"]})

with open(existing_list_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=["App", "Title"])
    writer.writeheader()
    writer.writerows(existing_list)

print(f"Added to existing list: {existing_list_path}")
