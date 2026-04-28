# ebook-list

전자책 목록을 수집하고 CSV로 정리하기 위한 스크립트 저장소입니다.

## 개요

Kindle, Ridibooks, Google Play Books, Kyobo 등 여러 소스의 전자책 목록을 정리하거나 병합하는 Python/PowerShell 스크립트가 포함되어 있습니다.

주요 파일:
- `generate_csv.py`: 통합 CSV 생성
- `generate_google_csv.py`, `generate_kindle_csv.py`, `generate_kyobo_only_csv.py`: 소스별 CSV 생성
- `fetch_ridibooks.py`, `extract_ridibooks.py`: Ridibooks 데이터 처리
- `add_kyobo.py`, `kyobo_covers.py`: 교보문고 관련 보조 작업

## 목적

- 전자책 보유 목록 정리
- 서점/앱별 목록을 CSV로 변환
- 개인 아카이브 또는 후속 분석용 데이터 준비

## 실행 예시

```bash
python generate_csv.py
python generate_google_csv.py
python generate_kindle_csv.py
```

생성 결과는 루트의 `*.csv` 파일들로 확인할 수 있습니다.
