import os
import datetime
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader

def convert_to_pdf(input_file_path, output_file_path):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    with open(input_file_path, 'r') as file:
        for line in file:
            pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(output_file_path)

def search_and_convert_files(src_directory, dest_directory, file_extension, start_date, end_date):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path)).date()

                if start_date <= creation_time <= end_date:
                    output_file_path = os.path.join(dest_directory, f"{os.path.splitext(file)[0]}.pdf")
                    convert_to_pdf(file_path, output_file_path)
                    print(f"Converted {file_path} to {output_file_path}")

if __name__ == "__main__":
    src_directory = "/path/to/source/directory"
    dest_directory = "/path/to/destination/directory"
    file_extension = ".txt"
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    search_and_convert_files(src_directory, dest_directory, file_extension, start_date, end_date)
