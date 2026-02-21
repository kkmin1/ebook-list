import os
import urllib.request
import re
import csv
import time
from html import unescape

def get_ridi_book_title(book_id):
    url = f"https://ridibooks.com/books/{book_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'<title>(.*?)</title>', html)
        if match:
            title = match.group(1).replace(' - 리디', '').replace(' - 소설', '').replace(' - 만화', '').replace(' - 전자책', '').strip()
            return unescape(title)
        return "Unknown Title"
    except Exception as e:
        return f"Error: {e}"

folder_path = r"C:\ebook\ridibooks\_3223830"
book_ids = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

results = []
for idx, book_id in enumerate(book_ids):
    print(f"Fetching {idx+1}/{len(book_ids)}: {book_id}")
    title = get_ridi_book_title(book_id)
    results.append({"App": "Ridibooks", "FolderID": book_id, "Title": title})
    time.sleep(0.5)

csv_path = r"C:\Users\kkmin\Desktop\ebook\ridibooks_extracted_list.csv"
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=["App", "FolderID", "Title"])
    writer.writeheader()
    writer.writerows(results)

print(f"Done! Saved to {csv_path}")
