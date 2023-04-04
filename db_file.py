import psycopg2
import random
import string



'''Class: To connect to the database.
        Function-1: connect_db:: Returns TRUE if connected or FALSE if not connected.
        Function-2: disconnect_db:: If connected, when called db will be disconnected.
        '''
        
#database calss to connect database
class Database():
        conn=None
        cursor=None

        def connect_db(self):
                try:
                        Database.conn=psycopg2.connect(host='139.59.61.252',database='lb_dev',user='nagaraja',password='#Tj42Xf8')
                        Database.cursor=Database.conn.cursor()
                        return True
                except:
                        return False

        def disconnect_db(self):
                Database.cursor.close()
                Database.conn.close()



class School():
       
        def get_all_school_name(self):
                query="SELECT school_code, school_name FROM main.school_detail;"
                try:
                        Database.cursor.execute(query)
                        temp = Database.cursor.fetchall()
                        school_details={}
                        for each in temp:
                                school_details.update({each[0]:each[1]})
                        return school_details

                except: 
                        return False
        
        

class Student(Database,School):
         
        def get_student_data(self):
                query="SELECT school_code, class,section,student_name,app_login_id FROM main.student_details;"
                try:

                        Database.cursor.execute(query)
                        temp = Database.cursor.fetchall()       #all student data from student database
                        school_data=super().get_all_school_name()       #all school_code and school_name from school_database
                        '''     School_code is key and school_name is value
                                ex:{12:'Lotus Public School'}
                        '''
                        student_data=[]         #will contains list of dict ( Student details )
                        for each_student in temp:
                                student={}             #each student data will be stored
                                student['School_name']=school_data[each_student[0]]     #school_name from school_data key. Also 'each_student[0]' is the school_code from student database
                                student['Class']=each_student[1]
                                student['Section']=each_student[2]
                                student['Name']=each_student[3]
                                student['Id']=each_student[4]
                                student_data.append(student)

                        return student_data
                except:
                        return False

# s=Student()
# s.connect_db()
# s.get_student_data()
# s.disconnect_db()