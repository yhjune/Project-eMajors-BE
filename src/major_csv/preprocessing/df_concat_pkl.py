import pickle
import pandas as pd

with open(file="introductions.pickle",mode='rb') as data:
    intro_df= pickle.load(data)

with open(file="majors.pickle",mode='rb') as data:
    majors_df = pickle.load(data)

with open(file="double_majors.pickle",mode='rb') as data:
    d_majors_df = pickle.load(data)

def convert_to_int(value):
    try:
        # Try to convert to integer
        return str(int(value))
    except (ValueError, TypeError):
        # Return the original value if conversion is not possible
        return value

def drop_condi(row):
    return f"{row['course_id']}_{row['department']}"

# rename columns
intro_df.rename(columns={'department_id':'department'},inplace=True)

# drop not required columns
majors_df = majors_df.drop(columns=["hour","2023_2nd_semester"])
d_majors_df = d_majors_df.drop(columns=["hour","2023_2nd_semester"])

# check NaN
majors_df['requried'] = majors_df['requried'].fillna('-')
majors_df['note'] = majors_df['note'].fillna('-')
d_majors_df['requried'] = d_majors_df['requried'].fillna('-')
d_majors_df['note'] = d_majors_df['note'].fillna('-')

# dfs department value unifying  df.loc[df['cid'] == 1, 'cid'] = 2
    # get csv 
file = '/Users/yhjune/Desktop/playground/major-csv/importdepartment.csv'
df = pd.read_csv(file)
    #  get a row in dataframe
for idx, r in df.iterrows():
    # change intro | major | dMajors = department
    depart = r['Department']
    i = r['Intro']
    m = r['Major']
    dm = r['dMajors']
    intro_df.loc[intro_df['department'] == i, 'department'] = depart
    majors_df.loc[majors_df['department'] == m, 'department'] = depart
    d_majors_df.loc[d_majors_df['department'] == dm, 'department'] = depart

# check duplicates
intro_df['course_id'] = intro_df['course_id'].apply(convert_to_int)
majors_df['course_id'] = majors_df['course_id'].apply(convert_to_int)
d_majors_df['course_id'] = d_majors_df['course_id'].apply(convert_to_int)
# introrow_df  = intro_df[intro_df['course_id']=='10018']
# majorsrow_df = majors_df[majors_df['course_id']=='10018']
# dmarow = d_majors_df[d_majors_df['course_id']=='10018']
# print(introrow_df)
# print(majorsrow_df)
# print(dmarow)

# merge intro_df, major, dmajors
merge1_df = intro_df.set_index('course_id').combine_first(majors_df.set_index('course_id')).reset_index() # intro_df 중심 major_df 병합 (intro_df에 없는 경우 nan )
merged2_df = intro_df.set_index('course_id').combine_first(d_majors_df.set_index('course_id')).reset_index()
result = pd.concat([merge1_df,merged2_df],ignore_index=True)

# drop duplicates
result['id_fields'] = result.apply(drop_condi, axis=1)
result.drop_duplicates(subset=['id_fields'],inplace=True,ignore_index=True)
result.drop(columns=['id_fields'],inplace=True)

#check NaN
    # intro_with_nulls = intro_df.isnull().sum()
    # print(intro_with_nulls)
    # majors_with_nulls = majors_df.isnull().sum()
    # print(majors_with_nulls)
    # d_majors_with_nulls = d_majors_df.isnull().sum()
    # print(d_majors_with_nulls)
result['note'] = result['note'].fillna('-')

# result_with_nulls = result.isnull().sum()
# print(result_with_nulls)


# result
intronum = result['intro_kr'].isnull().sum() # 584
courseintronum = len(intro_df['course_id']) # 2829
resultnum = len(result['course_id']) # 
row = result[result['course_id']=='20410']
print(row)
print(result)
print(intronum, resultnum-courseintronum)

# export result pickl, 
with open(file="result.pickle",mode='wb') as data:
    pickle.dump(result, data)