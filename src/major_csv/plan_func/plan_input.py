def user_major():
    user_major = input("당신의 전공은 무엇입니까? : ")
    second_major = input("복수 전공을 할 예정인가요? ( yes / no ) : ")
    
    if second_major.lower() == "yes":
        user_second_major = input("당신의 복수 전공은 무엇입니까? : ")
    elif second_major.lower() == "no":
        print("복수전공을 선택하지 않습니다.")
        user_second_major = "none"
    else:
        print("Invalid Input. please enter yes or no")
        exit()
    majors = [user_major, user_second_major]
    return majors

def user_semster(semester,result,course):
    if not isinstance(semester,int) : # int or arry[0] or array[0,1]
        user_semester = user_semester = semester[0]
        if len(semester) > 1: # arry[0] or array[0,1]
            print(course.get("name"), end =" : ")
            user_semester =int(input("몇학기에 들으시겠습니까? 1 or 2: "))
        if user_semester == 2 : 
            result["course"]["102"].append(course) 
        else: 
            result["course"]["101"].append(course)
    elif semester == 2:
        result["course"]["102"].append(course) 
    else:
        result["course"]["101"].append(course)

def user_lang():
    print("다음 중 어떤 것을 들으시겠습니까?")
    print("기본중국어(10563), 중급중국어(10133), 기본프랑스어(10564), 중급프랑스어(10565), 기본독일어(10566), 중급독일어(10130), 기본일본어(10570), 중급일본어(10132), 기본스페인어(10571), 중급스페인어(10665), 기본러시아어(10572)")
    user_lang = input("제 2외국어 선택 (ex. 기본중국어) : ")
    return user_lang