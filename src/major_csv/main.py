import csv_func
import os
from pathlib import Path

msg = "Roll the dice"
print(msg)


## ci , dm, m file path recusive
print("Getting file pahts...")
root = input("root : ") # all files must be nested in the root folder
output_path = root+"/"+input("output folder name: ")+"/" # exported csv files goes here

os.makedirs(output_path,exist_ok=True)

## cite
# print("Getting course introductions...")
# ci_pdf_files = Path(root).rglob('교과목기술_*.pdf')
# for idx, path in enumerate(ci_pdf_files):
#     path = str(path)
#     ci_csv_name = path.split('/')[-1].split('.')[0]+".csv"
#     csv_func.csv_funcs.course_introduction_csv(path,ci_csv_name, output_path)

# dm
print("Getting doule majors...")
dm_pdf_path =  Path(root).rglob('복수전공_*.pdf')
for idx, path in enumerate(dm_pdf_path):
    path = str(path)
    dm_csv_name = path.split('/')[-1].split('.')[0]+".csv"
    dm_condi_name = "S_condi_"+dm_csv_name.split("_")[-1]
    csv_func.csv_funcs.double_major_csv(path,dm_csv_name,dm_condi_name,output_path)

## m 
print("Getting majors...")
m_pdf_path = Path(root).rglob('주전공_*.pdf')
for idx, path in enumerate(m_pdf_path):
    path = str(path)
    m_csv_name = path.split('/')[-1].split('.')[0]+".csv"
    m_condi_name = "F_condi_"+m_csv_name.split("_")[-1]
    csv_func.csv_funcs.major_csv(path, m_csv_name, m_condi_name ,output_path)



print("Exporting csv finished")