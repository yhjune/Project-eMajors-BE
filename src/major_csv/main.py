import shell_func
from plan_func import *

client, db = shell_func.mongodb_client.start_client()
result = plan_instance.result()

department_collection = db['department']
course_collection = db['course']
courseintro_collection = db['course_intro']
liberal_collection = db['liberal_arts']


plan_print.all_department(department_collection)

majors = plan_input.user_major()
result.update({"major":majors[0], "d_major":majors[1]})

print(f'전공: {result["major"]} | 복수전공 : {result["d_major"]}')

m_college = plan_get.college(result["major"], department_collection)
libaral_arts = plan_get.libaral_arts(m_college, liberal_collection)

for key,semester in libaral_arts.items():
    if key != "_id" and semester != 0:
        # 제2외국어
        if key == "제2외국어" and semester != 0:
            user_lang = plan_input.user_lang()
            course_doc = plan_get.course_doc(user_lang)
            course = plan_get.cursor(course_doc) # 수업 찾음
            plan_input.user_semster(semester,result,course)
        # 기초교양
        course_doc =  plan_get.course_doc(key,course_collection)
        course = plan_get.cursor(course_doc)
        plan_input.user_semster(semester,result,course)
    else:
        continue

# 컴퓨팅
computing_docs = course_collection.find({"area":"컴퓨팅과수리적사고"})
plan_print.computings(computing_docs)
user_comput = input("\n위 목록 중 어느 것을 들으시겠습니까? ex) 논리와컴퓨터: ")
comput_doc = plan_get.course_doc(user_comput, course_collection)
for doc in comput_doc:
    course = doc["_id"]
    course.update({"name": doc["name"]})
    semester = doc["semester"]
    plan_input.user_semster(semester, result, course)

plan_print.result_libaral_arts(result)


client.close()