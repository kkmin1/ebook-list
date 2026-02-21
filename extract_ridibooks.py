"""
리디북스 epub 파일에서 책 제목 추출
epub 파일은 zip 형식이며 내부 OPF 파일에 메타데이터(제목, 저자)가 있음
"""
import os
import zipfile
import xml.etree.ElementTree as ET
import csv
from pathlib import Path

root_dir = Path(r"C:\ebook\ridibooks")
results = []

# 모든 .epub 파일 탐색
epub_files = list(root_dir.rglob("*.epub"))
print(f"발견된 epub 파일 수: {len(epub_files)}")

ns = {
    'opf': 'http://www.idpf.org/2007/opf',
    'dc':  'http://purl.org/dc/elements/1.1/',
}

for epub_path in epub_files:
    title = ""
    author = ""
    try:
        with zipfile.ZipFile(epub_path, 'r') as z:
            # container.xml → OPF 경로 찾기
            with z.open('META-INF/container.xml') as f:
                tree = ET.parse(f)
                rootfile = tree.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile')
                if rootfile is None:
                    rootfile = tree.find('.//{http://www.idpf.org/2007/opf}rootfile')
                opf_path = rootfile.attrib.get('full-path', '') if rootfile is not None else ''

            if not opf_path:
                # container.xml 없는 경우 직접 .opf 찾기
                opf_files = [n for n in z.namelist() if n.endswith('.opf')]
                opf_path = opf_files[0] if opf_files else ''

            if opf_path:
                with z.open(opf_path) as f:
                    opf_data = f.read()
                    opf_tree = ET.fromstring(opf_data)

                    # 여러 네임스페이스 시도
                    title_el = (
                        opf_tree.find('.//dc:title', ns) or
                        opf_tree.find('.//{http://purl.org/dc/elements/1.1/}title') or
                        opf_tree.find('.//title')
                    )
                    author_el = (
                        opf_tree.find('.//dc:creator', ns) or
                        opf_tree.find('.//{http://purl.org/dc/elements/1.1/}creator') or
                        opf_tree.find('.//creator')
                    )
                    title  = title_el.text.strip()  if title_el  is not None and title_el.text  else ""
                    author = author_el.text.strip() if author_el is not None and author_el.text else ""

    except Exception as e:
        title = f"[오류: {e}]"

    folder_id = epub_path.parent.name
    results.append({
        "App":     "Ridibooks",
        "FolderID": folder_id,
        "Title":   title if title else "(제목 없음)",
        "Author":  author,
        "File":    epub_path.name,
    })
    print(f"  {folder_id} → {title or '?'} / {author}")

# CSV 저장
out = r"C:\Users\kkmin\Desktop\ebook\ridibooks_list.csv"
with open(out, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=["App", "FolderID", "Title", "Author", "File"])
    writer.writeheader()
    writer.writerows(results)

print(f"\n✅ 총 {len(results)}권 → {out}")
