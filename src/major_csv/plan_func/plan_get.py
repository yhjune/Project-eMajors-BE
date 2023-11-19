
def college(major, department_collection):
    college = department_collection.find_one({"_id":major}).get("college")
    return college
        

def libaral_arts(college,liberal_collection):
    libaral_arts = liberal_collection.find_one({"_id":{"college":college}})
    return libaral_arts

def course_doc(name,course_collection):
    course_doc = course_collection.find({"name":name})
    return course_doc

def cursor(course_doc):
    for doc in course_doc:
        course = doc["_id"]
        course.update({"name": doc["name"]})
    return course

def course_intro(course_id,courseintro_collection):
    courses = courseintro_collection.find({"_id":{"course_id":course_id}})
    for course in courses:
        print(f'학수번호 :{course_id} | 과목명 : {course.get("course_name")} ')
        print(f'과목 설명 : {course.get("intro_kr")}')