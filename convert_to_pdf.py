import os
import glob
import subprocess

def convert_to_pdf(input_file, output_dir):
    """
    Convert a .doc or .docx file to .pdf using LibreOffice.
    """
    try:
        # Run LibreOffice in headless mode to convert the file to PDF
        command = [
            'libreoffice', '--headless', '--convert-to', 'pdf',
            '--outdir', output_dir, input_file
        ]
        subprocess.run(command, check=True)
        print(f"Converted {input_file} to PDF in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {input_file}: {e}")

def main():
    # Define directories
    doc_files_dir = 'doc_files'
    pdf_files_dir = 'pdf_files'

    # Create pdf_files directory if it doesn't exist
    if not os.path.exists(pdf_files_dir):
        os.makedirs(pdf_files_dir)

    # Get all .doc and .docx files in the doc_files directory
    doc_files = glob.glob(os.path.join(doc_files_dir, '*.doc'))
    docx_files = glob.glob(os.path.join(doc_files_dir, '*.docx'))

    # Convert all .doc and .docx files to .pdf
    for doc_file in doc_files + docx_files:
        convert_to_pdf(doc_file, pdf_files_dir)

if __name__ == "__main__":
    main()