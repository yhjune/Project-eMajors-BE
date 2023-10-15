import tabula
import pandas as pd

m_pdf_path = ''
m_csv_name = m_pdf_path.split('/')[-1].split('.')[0]+".csv"
m_condi_name = "F_condi_"+m_csv_name.split("_")[-1]

msg = "roll the dice"
print(msg)

df = tabula.read_pdf(m_pdf_path, pages="all",lattice=True, area=[199.7, 16 ,805.1, 579.8]) # read pdf
df_concat = pd.concat(df, ignore_index=True) # concast dataframe

df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고"] # colums name

df_concat = df_concat.drop(columns='학사편입생제외여부') # colum's details
df_concat.replace(r'\r','', regex=True, inplace=True) 
df_concat["구분"] = df_concat["구분"].ffill() 
df_concat["영역"] = df_concat['_id'].astype(str).replace(r'\d+',None,regex=True).ffill().replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-회]+','',regex=True)
df_concat["이수권장학년"] = df_concat["이수권장학년"].fillna(0).replace('계절',5).astype(int) # 이수 권장 학년 상관 없는 nan -> 0, 계절 학기 -> 5
df_concat["설정학기"] = df_concat["설정학기"].str.split(',')
df_concat = df_concat[["_id","구분","영역","교과목명","이수권장학년","설정학기","시간","학점","필수여부","개설학과","2023학년2학기개설여부","비고"]] # colum order

df_list = df_concat.dropna(subset=["시간"]).reset_index(drop=True) # 주전공 이수 과목 목록
df_list.to_csv(m_csv_name, mode="w") # 주전공 이수과목 목록 csv export

df_condi = df_concat[df_concat["교과목명"].notnull() & df_concat["교과목명"].str.contains("이수")].drop(columns=["구분","이수권장학년","설정학기","시간","학점","개설학과","2023학년2학기개설여부","영역"]).replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-후]+','',regex=True).reset_index(drop=True)
df_condi.columns = ["_id","이수조건","필수여부","비고"]
df_condi.to_csv(m_condi_name, mode="w") # 주전공 이수과목 조건 csv export 