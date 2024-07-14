---

# Project 3 - Generate PDF Python

## Overview
This Python script automates the creation of study notes in PDF format based on data provided in a CSV file (`topics.csv`). Each entry in the CSV file represents a topic with a specified number of pages, generating formatted PDF pages accordingly. This tool is designed for generating note templates or exporting CSV data into PDF formats for various purposes.

**Made during Learn Python 60 Days, Make 20 Apps**

## Requirements
- Python 3.x
- Libraries:
  - `fpdf` (to install: `pip install fpdf`)
  - `pandas` (to install: `pip install pandas`)

## Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your/repository.git
   cd project-3-generate-pdf-python
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Then install the required libraries:
   ```bash
   pip install fpdf pandas
   ```

3. **Prepare Input Data:**
   Edit the `topics.csv` file located in the project directory. This file specifies the study topics, their order, and the number of pages each topic should occupy.

   Example format of `topics.csv`:
   ```csv
   Order,Topic,Pages
   1,Variables,1
   2,Lists,1
   3,Functions,4
   4,While-loop,1
   5,Methods,1
   6,Match-case,1
   ```

4. **Run the Script:**
   Execute the Python script (`generate_notes.py`) to generate the PDF file:
   ```bash
   python generate_notes.py
   ```
   This command creates an `output.pdf` file in the project directory containing the study notes based on the information in `topics.csv`.

5. **Output:**
   The generated PDF (`output.pdf`) organizes study topics onto separate pages. Each topic starts on a new page and includes horizontal lines to facilitate note-taking.

## Customization
- **Adjust Text Size:** Modify the `text_size` variable in `generate_notes.py` to change the height of text lines in the PDF.
  
- **Formatting:** Customize fonts, colors, and layout by modifying parameters in the `define_header()`, `define_body_text()`, and `define_footer()` functions within the script.

## Notes
- Ensure the CSV file (`topics.csv`) is correctly formatted with headers and appropriate data types.
- The script assumes standard A4 paper format for PDF output. Modify the `format` parameter in `FPDF()` within the script if a different paper size is needed.

## Future Updates
Additional examples and enhancements may be added in future updates to expand functionality and customization options.


---
