# from openpyxl import Workbook
# from fastapi.responses import FileResponse
from app.model.student_model import Student

from app.utils.excel_decorator import export_excel

@export_excel(    sheet_name="Students",
    headers=["Id", "Name", "Age", "Course", "Teacher"],
    file_name="students.xlsx"
    )

def stu_cou_tech_excel_service(db):

    # wb = Workbook()
    # sheet = wb.active

    # sheet.title = "Students"

    # sheet["A1"] = "Id"
    # sheet["B1"] = "Name"
    # sheet["C1"] =  "Age"
    # sheet["D1"] =  "Course"
    # sheet["E1"] =  "Teacher"
    

    students = db.query(Student).all() #it is a object that contais students data

    print("________________",students)

    data = []
    # row = 2 # first row is headers so data shows from 2 row 
    for student in students:
        
        print(student.id, student.name, student.age)

        for course in student.courses:
#             sheet["A" + str(row)] = student.id
        
#             sheet["B" + str(row)] = student.name
        
#             sheet["C" + str(row)] = student.age

#             sheet["D" + str(row)] = course.course_name

#             sheet["E" + str(row)] = course.teacher.teacher_name
        

#         row = row + 1

#     wb.save("students.xlsx")

#     return FileResponse(
#     path="students.xlsx",
#     filename="students.xlsx",
#     media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# )

            data.append([
                student.id,
                student.name,
                student.age,
                course.course_name,
                course.teacher.teacher_name
            ])

    return data