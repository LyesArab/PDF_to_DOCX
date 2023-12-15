from pdf2docx import parse
from typing import Tuple
from tkinter import Tk, filedialog

def get_pdf_file_path():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring the file dialog to the front
    file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    root.destroy()
    return file_path

def convert_pdf2docs(input_file: str, output_file: str, pages: Tuple = None):
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file, docx_file=output_file, pages=pages)

    summary = {
        "File": input_file, "Pages": str(pages), "Output File": output_file
    }

    print("## Summary #########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("#####################################################################")
    return result

if __name__ == "__main__":
    import sys

    # Get the input PDF file dynamically using a file dialog
    input_file = get_pdf_file_path()

    # Provide default output file name
    output_file = "output.docx"

    convert_pdf2docs(input_file, output_file)
