"""
교보문고 커버 이미지를 모아서 HTML 갤러리로 만드는 스크립트
각 표지를 한 페이지에 모아 브라우저에서 OCR/시각 확인용
"""
import os
import base64
from pathlib import Path

medias_root = Path(r"C:\Users\Public\kyobo\eLibrary\B2C\Contents\Medias")
cover_paths = sorted(medias_root.glob("*/*/image/cover.jpg"))

html_parts = ["""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>교보 eBook 표지 목록</title>
<style>
  body { font-family: 'Malgun Gothic', sans-serif; background: #1a1a2e; color: #eee; margin: 0; padding: 20px; }
  h1  { text-align: center; color: #e94560; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 20px; }
  .card { background: #16213e; border-radius: 10px; overflow: hidden; text-align: center; padding-bottom: 8px; }
  .card img { width: 100%; height: 220px; object-fit: cover; }
  .card .code { font-size: 11px; color: #aaa; padding: 4px; word-break: break-all; }
</style>
</head>
<body>
<h1>📚 교보 eBook 표지 갤러리</h1>
<div class="grid">
"""]

for cover in cover_paths:
    folder_code = cover.parts[-4]  # e.g. 480D260286420
    with open(cover, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    html_parts.append(f"""  <div class="card">
    <img src="data:image/jpeg;base64,{b64}" alt="{folder_code}" />
    <div class="code">{folder_code}</div>
  </div>
""")

html_parts.append("</div></body></html>")

out_path = Path(r"C:\Users\kkmin\Desktop\ebook\kyobo_covers.html")
out_path.write_text("".join(html_parts), encoding="utf-8")
print(f"Done! {len(cover_paths)} covers → {out_path}")
