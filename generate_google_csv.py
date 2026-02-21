import csv

google_books = [
    {"App": "Google Play Books", "Title": "고구려 1 (도망자 을불)"},
    {"App": "Google Play Books", "Title": "전쟁과 평화"},
    {"App": "Google Play Books", "Title": "상도 (최인호)"},
    {"App": "Google Play Books", "Title": "상도 1 : 천하제일상"},
    {"App": "Google Play Books", "Title": "국화와 칼"},
    {"App": "Google Play Books", "Title": "고구려 2 (나의 창은 굽지 않는다)"},
    {"App": "Google Play Books", "Title": "고구려 3 (낙랑 축출)"},
    {"App": "Google Play Books", "Title": "고구려 4 (사유의 시대)"},
    {"App": "Google Play Books", "Title": "고구려 5 (백제의 칼)"},
    {"App": "Google Play Books", "Title": "고구려 6 (구부의 길)"},
    {"App": "Google Play Books", "Title": "미중전쟁 1"},
    {"App": "Google Play Books", "Title": "회의주의자를 위한 경제학"},
    {"App": "Google Play Books", "Title": "골고다 1"},
    {"App": "Google Play Books", "Title": "전쟁과 무기"},
    {"App": "Google Play Books", "Title": "무기체계 발달"},
    {"App": "Google Play Books", "Title": "경제학 혁명"},
    {"App": "Google Play Books", "Title": "서양 무기의 역사"},
    {"App": "Google Play Books", "Title": "전장을 지배한 무기전 전세를 뒤바꾼 보급전"},
    {"App": "Google Play Books", "Title": "살림지식총서 (여러 권)"},
    {"App": "Google Play Books", "Title": "리틀 라이프 1"},
    {"App": "Google Play Books", "Title": "리틀 라이프 2"},
    {"App": "Google Play Books", "Title": "안티프래질"},
    {"App": "Google Play Books", "Title": "절대적이며 상대적인 리더십의 물리학"},
    {"App": "Google Play Books", "Title": "상도 2"},
    {"App": "Google Play Books", "Title": "상도 3"},
    {"App": "Google Play Books", "Title": "가루전쟁"},
    {"App": "Google Play Books", "Title": "돈의 역사"},
    {"App": "Google Play Books", "Title": "50대 사건으로 보는 돈의 역사"},
    {"App": "Google Play Books", "Title": "대한민국 금융 잔혹사"},
    {"App": "Google Play Books", "Title": "경관의 피"},
    {"App": "Google Play Books", "Title": "탈세의 세계사"},
    {"App": "Google Play Books", "Title": "돈의 물리학"},
    {"App": "Google Play Books", "Title": "공작 1 (이중스파이 흑금성)"},
    {"App": "Google Play Books", "Title": "공작 2 (무간도에 갇힌 이중스파이)"},
    {"App": "Google Play Books", "Title": "인간실격"},
    {"App": "Google Play Books", "Title": "블랙 잭 (BLACK JACK)"},
    {"App": "Google Play Books", "Title": "흑치상지"},
    {"App": "Google Play Books", "Title": "탄금"},
    {"App": "Google Play Books", "Title": "삶의 정도"},
    {"App": "Google Play Books", "Title": "완전론"},
    {"App": "Google Play Books", "Title": "전쟁의 판도를 바꾼 전염병"},
    {"App": "Google Play Books", "Title": "파동의 법칙"},
    {"App": "Google Play Books", "Title": "슈뢰딩거의 파동방정식"},
    {"App": "Google Play Books", "Title": "C++ 관련 서적 (Accelerated C++)"},
    {"App": "Google Play Books", "Title": "필립 K. 딕 걸작선"},
]

filename = r"c:\Users\kkmin\Desktop\ebook\google_play_books_list.csv"
with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=["App", "Title"])
    writer.writeheader()
    writer.writerows(google_books)

print(f"File created: {filename}")
