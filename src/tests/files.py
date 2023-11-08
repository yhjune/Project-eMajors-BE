from pathlib import Path

ci_pdf_files = Path('/Users/yhjune/Desktop/playground/pdf/major_origin').rglob('주전공_*.pdf')

for idx, path in enumerate(ci_pdf_files):
    ci_pdf_path = str(path)
    ci_csv_name = ci_pdf_path.split('/')[-1].split('.')[0]+".csv"
    print(ci_pdf_path)