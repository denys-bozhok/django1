student = {
    "name" : "John", 
    "surname" : "Doe", 
    "skills" : {
        "html" : True , 
        "css" : True, 
        "js" : False, 
        "pythonFrameworks" : {
            "flask" : False, 
            "django" : {
                "django_rest_framework" : True, 
                "django" : {
                    "dtl" : True
                    }
                }
            }
        }
    }


def rec(student):
    
    for key, value in student.items():

        if type(value) == dict:
            return rec(value)

    return student

result = rec(student)
print(result)
