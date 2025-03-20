import os
import zipfile
from fpdf import FPDF
import pandas as pd

# Define the target size (68 KB)
TARGET_SIZE_BYTES = 68 * 1024  # 69632 bytes

# EICAR test string
EICAR_STRING = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# Function to generate a TXT file
def generate_txt(filename):
    with open(filename, "w") as f:
        f.write(EICAR_STRING)
    pad_file(filename)

# Function to generate a PDF file
def generate_pdf(filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    pdf.multi_cell(0, 10, EICAR_STRING)
    pdf.output(filename)
    pad_file(filename)

# Function to generate an Excel file (.xls and .xlsx)
def generate_excel(filename, ext):
    df = pd.DataFrame({"EICAR": [EICAR_STRING]})
    if ext == "xls":
        df.to_excel(filename, index=False, engine="xlwt")
    else:
        df.to_excel(filename, index=False, engine="openpyxl")
    pad_file(filename)

# Function to generate a ZIP file
def generate_zip(filename):
    zip_filename = filename.replace(".zip", "_content.txt")
    generate_txt(zip_filename)  # Create a TXT file to zip
    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(zip_filename, arcname="eicar_test.txt")
    os.remove(zip_filename)  # Clean up the temporary file
    pad_file(filename)

# Function to pad a file to exactly 68 KB
def pad_file(filename):
    with open(filename, "ab") as f:
        current_size = f.tell()
        padding_needed = TARGET_SIZE_BYTES - current_size
        if padding_needed > 0:
            f.write(b" " * padding_needed)  # Add empty bytes
    final_size = os.path.getsize(filename)
    print(f"Generated '{filename}' with size: {final_size} bytes (68 KB)")

# Function to prompt the user for file format
def prompt_for_format():
    format_choices = ["txt", "pdf", "xls", "xlsx", "zip"]
    print("\nChoose the format in which the 68 KB EICAR test file should be generated:")
    for i, fmt in enumerate(format_choices, 1):
        print(f"{i}. {fmt}")

    while True:
        choice = input("\nEnter the number (1-5) for format selection: ").strip()
        if choice in map(str, range(1, 6)):
            return format_choices[int(choice) - 1]
        print("Invalid choice. Please enter a number between 1 and 5.")

# Main function to generate the file
def main():
    selected_format = prompt_for_format()
    filename = f"eicar_test_68kb.{selected_format}"

    # Generate the file based on user choice
    if selected_format == "txt":
        generate_txt(filename)
    elif selected_format == "pdf":
        generate_pdf(filename)
    elif selected_format in ["xls", "xlsx"]:
        generate_excel(filename, selected_format)
    elif selected_format == "zip":
        generate_zip(filename)

if __name__ == "__main__":
    main()
