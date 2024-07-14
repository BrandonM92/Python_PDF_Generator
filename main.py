from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")
text_size = 14  # Adjust this number according to your preferred text height
page_count = 1
output_name = "output.pdf"  # Change this to whichever output name you want. Must end in .pdf


def define_header(extra_page):
    """This method defines the header for each page. If it is the start of a new topic it will display the header by
    calling it with the number 0, otherwise give it any other number, and it will call everything but the header
    text. """
    pdf.add_page()
    if extra_page == 0:
        pdf.set_font(family="Times", style="B", size=20)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=20, txt=row['Topic'], align="C", ln=1)
        pdf.line(x1=10, y1=25, x2=200, y2=25)
    else:
        pdf.set_font(family="Times", style="B", size=20)
        pdf.set_text_color(100, 100, 100)
        pdf.line(x1=10, y1=25, x2=200, y2=25)


def define_body_text():
    """This method is responsible for the creation of the body of each page. Lines are drawn starting from below the
    header and will go by a pre-determined increment that can be adjusted as you increase/decrease text size you will
    decrease/increase the range counter respectively.
    Note:The bigger the text the lower the counter, and vice versa.
    """
    y_increment = 25  # Starting position for lines
    for x in range(19):  # Draw 18 lines per page
        pdf.line(x1=10, y1=y_increment, x2=200, y2=y_increment)
        y_increment += text_size


def define_footer(page_counter):
    """This method handles the implementation of the footer, which includes a running counter for page count as well
    as a reference to the topic at the bottom of the page."""
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(140, 140, 140)
    pdf.set_xy(10, 275)  # Adjust Y position for footer as needed
    pdf.cell(w=0, h=10, txt=row["Topic"], align="L")
    pdf.cell(w=0, h=10, txt=str(page_counter), align="R")
    return page_counter + 1



"""This is the primary portion of the code that utilizes all the methods and outputs a pdf file.
    Note: Each time you run the program the PDF file called "Output.pdf" will overwrite it's previous version.
    """
for index, row in df.iterrows():
    define_header(0)
    define_body_text()
    page_count = define_footer(page_count)

    # If more than one page is required for the topic, add additional pages
    for _ in range(row["Pages"] - 1):
        define_header(1)
        define_body_text()
        page_count = define_footer(page_count)

pdf.output(output_name)
