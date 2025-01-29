
# Document to PDF Converter

This Python script converts `.doc` and `.docx` files into `.pdf` format using LibreOffice. It is designed to work on Linux systems, specifically Ubuntu/KDE.

## Features

* Converts `.doc` and `.docx` files to `.pdf`.
* Automatically processes all files in a specified input directory (`doc_files`).
* Saves the converted `.pdf` files in a specified output directory (`pdf_files`).
* Uses LibreOffice for headless conversion, ensuring compatibility with Linux systems.

---

## Prerequisites

Before using this script, ensure the following dependencies are installed:

### 1. **LibreOffice**

LibreOffice is required for converting `.doc` and `.docx` files to `.pdf`. Install it using the following command:

bash

Copy

```
sudo apt update
sudo apt install libreoffice
```

### 2. **Python 3**

The script is written in Python 3. Ensure Python 3 is installed on your system. You can check by running:

bash

Copy

```
python3 --version
```

If Python 3 is not installed, install it using:

bash

Copy

```
sudo apt install python3
```

---

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the project directory:

bash

Copy

```
cd /path/to/project
```

3. Ensure the required dependencies (LibreOffice and Python 3) are installed as described above.

---

## Usage

### Directory Structure

Before running the script, organize your files as follows:

Copy

```
.
├── doc_files/               # Input directory for .doc and .docx files
│   ├── document1.doc
│   ├── document2.docx
├── pdf_files/               # Output directory for converted .pdf files
└── convert_to_pdf.py        # The Python script
```

* Place all `.doc` and `.docx` files you want to convert into the `doc_files` directory.
* The `pdf_files` directory will be created automatically if it doesn't exist. All converted `.pdf` files will be saved here.

### Running the Script

Run the script using the following command:

bash

Copy

```
python3 convert_to_pdf.py
```

### Output

After running the script, the `pdf_files` directory will contain the converted `.pdf` files:

Copy

```
.
├── doc_files/
│   ├── document1.doc
│   ├── document2.docx
├── pdf_files/
│   ├── document1.pdf
│   ├── document2.pdf
└── convert_to_pdf.py
```

---

## Customization

### Input and Output Directories

You can customize the input and output directories by modifying the following lines in the script:

python

Copy

```
doc_files_dir = 'doc_files'  # Input directory for .doc and .docx files
pdf_files_dir = 'pdf_files'  # Output directory for converted .pdf files
```

### Supported File Formats

The script currently supports `.doc` and `.docx` files. If you need to add support for other formats (e.g., `.odt`), you can modify the `glob` patterns in the script:

python

Copy

```
doc_files = glob.glob(os.path.join(doc_files_dir, '*.doc'))
docx_files = glob.glob(os.path.join(doc_files_dir, '*.docx'))
```

---

## Troubleshooting

### 1. **LibreOffice Not Found**

If you encounter an error like `libreoffice: command not found`, ensure LibreOffice is installed correctly. Test it by running:

bash

Copy

```
libreoffice --version
```

If the command is not found, reinstall LibreOffice:

bash

Copy

```
sudo apt install --reinstall libreoffice
```

### 2. **Permission Denied**

If you see a `Permission denied` error, ensure the script has execute permissions. Run:

bash

Copy

```
chmod +x convert_to_pdf.py
```

### 3. **Conversion Fails**

If a file fails to convert, ensure it is not corrupted and is in a supported format (`.doc` or `.docx`). You can also try converting the file manually using LibreOffice to debug the issue.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## Author

Matheus Libanio

matheus.alibanio@usp.br

github.com/matheuslibanio
