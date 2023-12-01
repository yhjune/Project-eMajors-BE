from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

today_date = datetime.now().date()

title = "Erode"
user_name = "hyojung"
date = today_date.strftime("%Y-%m-%d")
print(f'{title} {user_name} {date}')

major = "major1"
double_major = "moajor2"

def create_horizontal_pdf(file_path, data):
    # Create a PDF document with landscape orientation
    doc = SimpleDocTemplate(file_path, pagesize=(letter[1], letter[0]))

    # Create a list to hold the content
    content = []

    # Calculate the available width and height for the content
    page_width, page_height = doc.pagesize
    available_width = page_width - doc.leftMargin - doc.rightMargin
    available_height = page_height - doc.bottomMargin - doc.topMargin

    # Create a table with a single row to hold the list items horizontally
    table_data = [[item] for item in data]
    table = Table(table_data)

    # Apply styles to the table
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # Add the table to the content
    content.append(table)

    # Build the PDF document
    doc.build(content)

if __name__ == "__main__":
    
    my_list = [{"Item1", "tems"}, "Item 2", "Item 3", "Item 4"]

    pdf_file_path = "horizontal_output.pdf"
    create_horizontal_pdf(pdf_file_path, my_list)

    print(f"Horizontal PDF created successfully at {pdf_file_path}")
