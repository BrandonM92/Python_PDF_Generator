from fpdf import FPDF
import pandas as pd

"""
    If you want to pre-make studying notes, you can edit the topics.csv and specify
    header for each section and how many pages you want it to take.
"""
pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")
page_count = 0

for index, row in df.iterrows():
    content = f"{row['Topic']}"
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=content, align="C", ln=1)
    pdf.line(x1=10,y1=28,x2=200,y2=28)
    # pdf.cell(w=0, h=10, txt=str(page_count), align="B", ln=1)
    # page_count += 1

# w - Width, h - height of cell, txt- text within cell
# align is how you want to align content
# ln is how many lines, leave at 1
# border is the border density

pdf.output("output.pdf")
