from db_file import Student
import json


def get_student_details():
        s=Student()
        if(not s.connect_db()):
            return False
        student_data=s.get_student_data()
        if(not student_data):
            s.disconnect_db()
            return False
        else:
            s.disconnect_db()
            # print(len(student_data))
            #convertting student_data (List of dict) into json string  
            student_data=json.dumps(student_data,indent=4) 
            return student_data


# print(get_student_details())