def all_department(department_collection):
    department_docs = department_collection.find({})
    for doc in department_docs:
        department, college = doc.get('_id'), doc.get('college')
        print(f'학과 : {department} | 대학: {college}')

def result(result):
    for index , value in result.items():
        if index == "course":
            for semester, courses in value.items():
                names = []
                for _, name in enumerate(courses):
                    names.append(name.get("name"))
                print(f'{semester} : {names}')
        else: 
            continue

def computings(computing_docs):
    for doc in computing_docs:
        print(doc["name"], end=" | ")
        