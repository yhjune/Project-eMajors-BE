import tabula
import pandas as pd
import numpy as np

root = '/Users/yhjune/Desktop/playground/pdf/'

output_path = root+'resutls/'
m_pdf_path = root+'major_origin/인공지능대학/주전공_인공지능학과.pdf'
m_csv_name = m_pdf_path.split('/')[-1].split('.')[0]+".csv"
m_condi_name = "F_condi_"+m_csv_name.split("_")[-1]

def major_df(m_pdf_path):

    df = tabula.read_pdf(m_pdf_path, pages="all",lattice=True, area=[163.3, 17.4 ,802.9, 579.0]) # read pdf
    df_concat = pd.concat(df, ignore_index=True).dropna(thresh=4) # concast dataframe

    if len(df_concat.columns)==13:
        df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고","교과과정안내"] # colums name
    else: df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고"]
    
    df_concat = df_concat.drop(columns='학사편입생제외여부') # colum's details
    df_concat.replace(r'\r','', regex=True, inplace=True)
    df_concat["구분"] = df_concat["구분"].ffill()
    df_concat["영역"] = df_concat['_id'].astype(str).replace(r'\d+',None,regex=True).ffill().replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-회]+','',regex=True)
    df_concat["이수권장학년"] = df_concat["이수권장학년"].fillna(0).replace('계절',5).astype(int) # 이수 권장 학년 상관 없는 nan -> 0, 계절 학기 -> 5
    df_concat["설정학기"] = df_concat["설정학기"].astype(str).str.split(',')
    df_concat = df_concat[["_id","구분","영역","교과목명","이수권장학년","설정학기","시간","학점","필수여부","개설학과","2023학년2학기개설여부","비고"]] # colum order

    # 주전공 이수 과목 목록
    df_list = df_concat.dropna(subset=["시간"]).reset_index(drop=True)
    df_list.columns = ["course_id", "classification", "area", "course_name", "academic_year", "semester","hour","credit","requried","department","2023_2nd_semester","note"]

    # 주전공 이수과목 조건
    df_condi = df_concat[df_concat["교과목명"].notnull() & df_concat["교과목명"].str.contains("이수")].drop(columns=["구분","이수권장학년","설정학기","시간","학점","개설학과","2023학년2학기개설여부","영역"]).replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-후]+','',regex=True).reset_index(drop=True)
    df_condi.columns = ["area","condition","requried","note"]

    return df_list, df_condi

def f_condi_doc(dataframe): # dataframe = df_condi
    new_f_condis = []
    for row in dataframe.itertuples():
        
        f_condi ={

        }
    return new_f_condis

def m_course_doc(dataframe): # dataframe = df_list
    new_courses =[]
    for row in dataframe.itertuples():
        course_id, classification, department_id, credit, course_name = row.course_id, row.classification, row.department,row.credit,row.course_name
        course = {
            "_id" : course_id,
            "department_id" : department_id,
            "name" : course_name,
            "classification": classification,
            "credit": credit
        }
        new_courses.append(course)
    return new_courses


def revise_major_df(m_pdf_path):

    df = tabula.read_pdf(m_pdf_path, pages="all",lattice=True, area=[163.3, 17.4 ,802.9, 579.0]) # read pdf
    df_concat = pd.concat(df, ignore_index=True).dropna(thresh=2) # concast dataframe dropna(thresh=4)

    df_concat.to_csv(output_path+"classifi.csv",mode='w')

    if len(df_concat.columns)==13:
        df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고","교과과정안내"] # colums name
    else: df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고"]
    
    df_concat = df_concat.drop(columns='학사편입생제외여부') # colum's details
    df_concat.replace(r'\r','', regex=True, inplace=True) 
    df_concat["구분"] = df_concat["구분"].ffill()
    
    # df_concat["영역"] = df_concat['_id'].astype(str).replace(r'\d+',None,regex=True).ffill().replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-회]+','',regex=True)
    df_concat["영역"] = df_concat['_id'].astype(str).replace(r'\d+',np.NaN,regex=True).ffill().replace(r'[\[\]\-\#\(\)]+','',regex=True)

    
    df_concat["이수권장학년"] = df_concat["이수권장학년"].fillna(0).replace('계절',5).astype(int) # 이수 권장 학년 상관 없는 nan -> 0, 계절 학기 -> 5
    df_concat["설정학기"] = df_concat["설정학기"].astype(str).str.split(',')
    
    
    df_concat = df_concat[["_id","구분","영역","교과목명","이수권장학년","설정학기","시간","학점","필수여부","개설학과","2023학년2학기개설여부","비고"]] # colum order

    # 주전공 이수 과목 목록
    df_list = df_concat.dropna(subset=["시간"]).reset_index(drop=True)
    df_list.columns = ["course_id", "classification", "area", "course_name", "academic_year", "semester","hour","credit","requried","department","2023_2nd_semester","note"]

    # 주전공 이수과목 조건
    df_condi = df_concat[df_concat["교과목명"].notnull() & df_concat["교과목명"].str.contains("이수")].drop(columns=["구분","이수권장학년","설정학기","시간","학점","개설학과","2023학년2학기개설여부","영역"]).replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-후]+','',regex=True).reset_index(drop=True)
    df_condi.columns = ["area","condition","requried","note"]

    return df_list, df_condi


print(revise_major_df(m_pdf_path))

df_list , df_condi = revise_major_df(m_pdf_path)

df_condi.to_csv(output_path+"condi.csv",mode='w')