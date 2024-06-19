import sys
import os
import fitz  # pip install PyMuPDF


def remove_rect_from_pdf(input_pdf, output_pdf):
    # Open the input PDF file
    pdf_document = fitz.open(input_pdf)

    # Iterate through each page
    for page in pdf_document:
        # Get the drawings on the page
        paths = page.get_drawings()
        # Iterate through each drawing and add a redact annotation
        for path in paths:
            rect = path["rect"]
            page.add_redact_annot(rect)
        # Apply redactions to the page
        page.apply_redactions(0, 2, 1)

    # Save the modified PDF to the output path
    pdf_document.save(output_pdf)
    pdf_document.close()


def main():
    if len(sys.argv) != 2:
        print("Usage: rectrm <input_pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    if not os.path.exists(input_pdf):
        print(f"File not found: {input_pdf}")
        sys.exit(1)

    # Generate output file name
    output_pdf = os.path.splitext(input_pdf)[0] + "_output.pdf"

    # Process the PDF
    remove_rect_from_pdf(input_pdf, output_pdf)
    print(f"Processed: {input_pdf}")
    print(f"Output saved to: {output_pdf}")


if __name__ == "__main__":
    main()
