from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas 
from app.student.student_model import Student
from reportlab.platypus import Table , SimpleDocTemplate , TableStyle 
from reportlab.lib import colors


def stu_cou_tech_pdf_service(db):

    doc = SimpleDocTemplate("students.pdf") #titile for doc 

    # c.drawString(250, 800, "Student Report")

    # c.drawString(50, 760, "ID")
    # c.drawString(150, 760, "Name")
    # c.drawString(300, 760, "Age")
    
    data = [
        ["ID" , "Name", "Age" , "Course" , "Teacher"]
    ]
    students = db.query(Student).all()

    # y = 730

    for student in students:

        for course in student.courses:

        # c.drawString(50, y, str(student.id))
        # c.drawString(150, y, student.name)
        # c.drawString(300, y, str(student.age))

        # y -= 20

    # c.save()
            data.append([
                student.id,
                student.name,
                student.age,
                course.course_name,
                course.teacher.teacher_name
            ])
    
    table = Table(data,
                  colWidths=(50,150,60,150,150))

    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    doc.build([table])

    return FileResponse(
        path="students.pdf",
        filename="students.pdf",
        media_type="application/pdf"
    )



