
# Rectrm PDF Tool

`rectrm` is a command-line tool for removing rectangular drawings from PDF files. It simplifies the process of redacting specific regions from a PDF document.

## Features

- **Redacts rectangular regions**: Automatically detects and redacts rectangular drawing elements from PDF files.
- **Easy to use**: Provides a simple command-line interface.
- **Standalone executable**: No need for Python to be installed; a standalone executable can be created.

## Usage

To use `rectrm`, run the executable with the path to the input PDF file. The output will be saved as `<input_pdf>_output.pdf`.

```sh
./rectrm <input_pdf>
```

## Example

```sh
./rectrm sample.pdf
```

This command processes `sample.pdf` and saves the result as `sample_output.pdf`.

## Installation

### Clone the Repository

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/sk-226/rectrm-pdf-tool.git
    ```

2. Navigate to the project directory:

    ```sh
    cd rectrm-pdf-tool
    ```

### Building the Executable

To build the executable from the Python script using `PyInstaller`, follow these steps:

1. Install `PyInstaller` and `PyMuPDF` if they are not already installed:

    ```sh
    pip install pyinstaller PyMuPDF
    ```

2. Run the following command to create the executable:

    ```sh
    pyinstaller --onefile rectrm.py
    ```

This will generate the executable in the `dist` directory.
