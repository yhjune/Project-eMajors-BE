import tabula
import pandas as pd

msg = "course introduction"

def course_introduction_csv(ci_pdf_path, ci_csv_name, output_path):
    df = tabula.read_pdf(ci_pdf_path, pages= "all", lattice=True, area=[135.3, 15.3 ,563.6 , 822.5]) #PDF 읽어오기
    df_concat = pd.concat(df, ignore_index=True)

    df_concat.columns = ["순번","설정전공","_id","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"] # colums name

    df_concat.replace(r'\r','', regex=True ,inplace=True) # colum's deails
    df_concat.reset_index(drop=True, inplace=True)
    df_concat.drop(columns="순번")

    df_concat = df_concat[["_id","설정전공","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"]] # colum order 

    df_concat.to_csv(output_path+ci_csv_name, mode="w") # export csv
    return print(msg + ': ' +ci_csv_name)
