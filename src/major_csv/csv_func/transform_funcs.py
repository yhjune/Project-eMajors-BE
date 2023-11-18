import tabula
import pandas as pd
import numpy as np

def course_intro_df(ci_pdf_path, ci_csv_name, output_path):
    msg = "course introduction"
    
    df = tabula.read_pdf(ci_pdf_path, pages= "all", lattice=True, area=[135.3, 15.3 ,563.6 , 822.5]) #PDF 읽어오기
    df_concat = pd.concat(df, ignore_index=True)

    df_concat.columns = ["순번","설정전공","_id","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"] # colums name

    df_concat.replace(r'\r','', regex=True ,inplace=True) # colum's deails
    df_concat.reset_index(drop=True, inplace=True)
    df_concat.drop(columns="순번")

    df_concat = df_concat[["_id","설정전공","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"]] # colum order

    df_concat.columns = ["course_id", "department_id", "course_name","course_name_eng","intro_kr","intro_eng"]
    df_concat['course_id'] = df_concat['course_id'].astype("int")
    df_concat = df_concat.astype("str")

    return df_concat

def ci_course_doc(dataframe):
    new_courses = []

    for row in dataframe.itertuples():
        course_id, department_id, course_name = row.course_id, row.department_id, row.course_name
        course  ={ 
            "_id" : course_id,
            "department_id" : department_id,
            "name" : course_name,
            "classification": '',
            "credit": ''
        }
        new_courses.append(course)
    return new_courses

def ci_course_intro_doc(dataframe):
    new_course_intros = []
    for row in dataframe.itertuples():
        course_id, department_id, course_name, course_name_eng, intro_kr, intro_eng = row.course_id, row.department_id, row.course_name, row.course_name_eng, row.intro_kr, row.intro_eng
        course_intro = {
            "course_id" : course_id,
            "department_id" : department_id,
            "course_name" : course_name,
            "intro_kr": intro_kr ,
            "intro_eng": intro_eng ,
            "academic_year": '',
            "course_name_eng" : course_name_eng 
        }
        new_course_intros.append(course_intro)
    
    return new_course_intros

def course_introduction_csv(ci_pdf_path, ci_csv_name, output_path):
    msg = "course introduction"
    
    df = tabula.read_pdf(ci_pdf_path, pages= "all", lattice=True, area=[135.3, 15.3 ,563.6 , 822.5]) #PDF 읽어오기
    df_concat = pd.concat(df, ignore_index=True)

    df_concat.columns = ["순번","설정전공","_id","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"] # colums name

    df_concat.replace(r'\r','', regex=True ,inplace=True) # colum's deails
    df_concat.reset_index(drop=True, inplace=True)
    df_concat.drop(columns="순번")

    df_concat = df_concat[["_id","설정전공","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"]] # colum order 

    df_concat.to_csv(output_path+ci_csv_name, mode="w") # export csv
    return print(msg + ': ' +ci_csv_name)


def double_major_df(dm_pdf_path,dm_csv_name,dm_condi_name,output_path):
    msg = "double major"
    
    df = tabula.read_pdf(dm_pdf_path, pages="all",lattice=True, area=[163.5, 13,802.1,580.5]) # read pdf (head include)
    df_concat = pd.concat(df, ignore_index=True).dropna(thresh=4) # concat dataframe, drop rows na < 4 

    if len(df_concat.columns)==13:
        df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고","교과과정안내"] # colums name
    else: df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고"]

    df_concat = df_concat.drop(columns='학사편입생제외여부') # colum's details
    df_concat.replace(r'\r','', regex=True, inplace=True)
    df_concat["구분"] = df_concat["구분"].ffill()
    df_concat["영역"] = df_concat['_id'].astype(str).replace(r'\d+',np.nan,regex=True).ffill().replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-핳]','',regex=True)
    df_concat["이수권장학년"] = df_concat["이수권장학년"].fillna(0).replace('계절',5).astype(int)

    df_concat["설정학기"] = df_concat["설정학기"].astype(str).str.split(',')

    df_concat = df_concat[["_id","구분","영역","교과목명","이수권장학년","설정학기","시간","학점","필수여부","개설학과","2023학년2학기개설여부","비고"]] # colum order

    # 복수 전공 이수 과목 목록
    df_list = df_concat.dropna(subset=["시간"]).reset_index(drop=True) 
    df_list.columns = ["course_id","classification","area","course_name","academic_year","semester","hour","credit","required","department","2023_2nd_semester","note"]

    # 복수전공 이수 조건 
    df_condi = df_concat[df_concat["교과목명"].notnull() & df_concat["교과목명"].str.contains("이수")].drop(columns=["구분","이수권장학년","설정학기","시간","학점","개설학과","2023학년2학기개설여부","영역"]).replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-후]+','',regex=True).reset_index(drop=True)
    df_condi.columns = ["area","condition","required","note"]
    
    return df_list, df_condi

def dm_course_doc(dataframe): # dataframe = df_list
    new_courses =[]
    for row in dataframe.itertuples():
        course_id, classification, department_id, credit, course_name = row.course_id, row.classification, row.department,row.credit,row.course_name
        course={
            "_id" : course_id,
            "department_id" : department_id,
            "name" : course_name,
            "classification": classification,
            "credit": credit
        }
        new_courses.append(course)
    return new_courses

def double_major_csv(dm_pdf_path,dm_csv_name,dm_condi_name,output_path):
    msg = "double major"
    
    df = tabula.read_pdf(dm_pdf_path, pages="all",lattice=True, area=[163.5, 13,802.1,580.5]) # read pdf (head include)
    df_concat = pd.concat(df, ignore_index=True).dropna(thresh=4) # concat dataframe, drop rows na < 4 

    if len(df_concat.columns)==13:
        df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고","교과과정안내"] # colums name
    else: df_concat.columns = ["구분","_id","교과목명","이수권장학년","설정학기","시간","학점","필수여부","학사편입생제외여부","개설학과","2023학년2학기개설여부","비고"]

    df_concat = df_concat.drop(columns='학사편입생제외여부') # colum's details
    df_concat.replace(r'\r','', regex=True, inplace=True)
    df_concat["구분"] = df_concat["구분"].ffill()
    df_concat["영역"] = df_concat['_id'].astype(str).replace(r'\d+',np.nan,regex=True).ffill().replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-핳]','',regex=True)
    df_concat["이수권장학년"] = df_concat["이수권장학년"].fillna(0).replace('계절',5).astype(int)

    df_concat["설정학기"] = df_concat["설정학기"].astype(str).str.split(',')

    df_concat = df_concat[["_id","구분","영역","교과목명","이수권장학년","설정학기","시간","학점","필수여부","개설학과","2023학년2학기개설여부","비고"]] # colum order

    df_list = df_concat.dropna(subset=["시간"]).reset_index(drop=True) # 복수 전공 이수 과목 목록
    df_list.to_csv(output_path+dm_csv_name, mode="w") # export csv

    df_condi = df_concat[df_concat["교과목명"].notnull() & df_concat["교과목명"].str.contains("이수")].drop(columns=["구분","이수권장학년","설정학기","시간","학점","개설학과","2023학년2학기개설여부","영역"]).replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-후]+','',regex=True).reset_index(drop=True)
    df_condi.columns = ["_id","이수조건","필수여부","비고"] # 복수전공 이수 조건 
    df_condi.to_csv(output_path+dm_condi_name, mode="w") # export csv
    return print(msg+': '+dm_csv_name)


def major_df(m_pdf_path, m_csv_name, m_condi_name, output_path):

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

def major_csv(m_pdf_path, m_csv_name, m_condi_name, output_path):
    msg = "major"
    
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

    df_list = df_concat.dropna(subset=["시간"]).reset_index(drop=True) # 주전공 이수 과목 목록
    df_list.to_csv(output_path+m_csv_name, mode="w") # 주전공 이수과목 목록 csv export

    df_condi = df_concat[df_concat["교과목명"].notnull() & df_concat["교과목명"].str.contains("이수")].drop(columns=["구분","이수권장학년","설정학기","시간","학점","개설학과","2023학년2학기개설여부","영역"]).replace(r'[^A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-후]+','',regex=True).reset_index(drop=True)
    df_condi.columns = ["_id","이수조건","필수여부","비고"]
    df_condi.to_csv(output_path+m_condi_name, mode="w") # 주전공 이수과목 조건 csv export 

    return print(msg +': '+m_csv_name)


