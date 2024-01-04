from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

date = datetime.now().date().strftime("%Y-%m-%d")
title = "학과목 예상 로드맵"
user_name = "hyojung"
major = "major1"
double_major = "major2"
pdf_file_path = "report.pdf"
print(f"{title} {user_name} {date}")


def get_body_style():
    style = getSampleStyleSheet()
    body_style = style["BodyText"]
    body_style.fontSize = 20
    return body_style


def create_pdf(file_path, data):
    # Create a PDF document with landscape orientation
    doc = SimpleDocTemplate("report.pdf", pagesize=A4)
    style = getSampleStyleSheet()
    body_style = get_body_style()
    # if you want to see all the sample styles, this prints them with `style.list()`
    content = []
    head_table = Table(data)
    head_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 1), (0, 2), colors.lightgrey),
                ("BACKGROUND", (2, 1), (2, 2), colors.lightgrey),
                ("BACKGROUND", (4, 1), (4, 1), colors.lightgrey),
                ("BACKGROUND", (6, 1), (6, 1), colors.lightgrey),
                ("GRID",(0,0),(0,0),1,colors.lightgrey),
                ("GRID",(0,1),(7,2),1,colors.black),
                ("SPAN",(4,2),(7,2))
            ]
        )
    )
    body_table = Table([["course_id", "credit", "area", "course_name(kr)", "name(en)","note"],[]])
    body_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (5, 0), colors.lightgrey),
                ("GRID",(0,0),(5,1),1,colors.black)
            ]
        )
    )
    content.append(head_table)
    content.append(body_table)
    doc.build(content)

if __name__ == "__main__":
    data = [
        [title],
        [
            "college",
            "college_name",
            "department",
            "department_name",
            "major",
            major,
            "double_major",
            double_major,
        ],
        ["date", date, "namecol", "name"],
    ]
    create_pdf(pdf_file_path, data)
    print("pdf created")
