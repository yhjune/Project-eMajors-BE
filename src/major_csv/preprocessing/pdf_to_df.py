from pathlib import Path
import csv_func
import pandas as pd

# ci , dm, m file path recusive
print("...Getting file pahts...")
root = input("root : ") # all files must be nested in the root folder

# Course_introduction.pdf
ci_course_docs =[]
ci_courseintro_docs = []

df1=pd.DataFrame()
print("...Getting course introductions...")
ci_pdf_files = Path(root).rglob('교과목기술_*.pdf')
for idx, path in enumerate(ci_pdf_files):
    path = str(path)
    ci_name = path.split('/')[-1].split('.')[0]
    print(f'now processing : {ci_name}')
    df = csv_func.transform_funcs.course_intro_df(path)
    ci_course_docs.append(df)
    
# major.pdf
m_course_docs = []
df2=pd.DataFrame()
print("Getting majors...")
m_pdf_path = Path(root).rglob('주전공_*.pdf')
for idx, path in enumerate(m_pdf_path):
    path = str(path)
    m_csv_name = path.split('/')[-1].split('.')[0]
    print(f'now processing : {m_csv_name}')
    df_list, df_condi = csv_func.transform_funcs.major_df(path)
    m_course_docs.append(df_list)

#double_major.pdf
df3 = pd.DataFrame()
dm_course_docs = []
print("...Getting double majors...")
dm_pdf_path =  Path(root).rglob('복수전공_*.pdf')
for idx, path in enumerate(dm_pdf_path):
    path = str(path)
    dm_csv_name = path.split('/')[-1].split('.')[0]
    print(f'now processing : {dm_csv_name}')
    df_list, df_condi = csv_func.transform_funcs.double_major_df(path)
    dm_course_docs.append(df_list)

df2 = pd.concat(m_course_docs,ignore_index=True)
df1 = pd.concat(ci_course_docs,ignore_index=True)
df3 = pd.concat(dm_course_docs,ignore_index=True)

print(f'total course intro : {len(df1)}')
print(f'total course intro : {len(df2)}')
print(f'total course intro : {len(df3)}')

print(df1.head())
print(df2.head())
print(df3.head())