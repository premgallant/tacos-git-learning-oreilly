import pymupdf  # PyMuPDF
import hashlib

def compare_pdfs_with_hashing(old_pdf_path, new_pdf_path):
    """
    Compares two PDFs with page rearrangements using hashing.

    Args:
        old_pdf_path (str): Path to the older PDF file.
        new_pdf_path (str): Path to the newer PDF file.
    """

    old_doc = pymupdf.open(old_pdf_path)
    new_doc = pymupdf.open(new_pdf_path)

    old_page_hashes = {}
    for page_num in range(old_doc.page_count):
        text = old_doc[page_num].get_text()
        old_page_hashes[page_num] = hashlib.md5(text.encode()).hexdigest()

    for page_num in range(new_doc.page_count):
        text = new_doc[page_num].get_text()
        new_page_hash = hashlib.md5(text.encode()).hexdigest()

        match_found = False
        for old_page_num, old_hash in old_page_hashes.items():
            if new_page_hash == old_hash:
                print(f"Page {page_num + 1} in the new PDF matches page {old_page_num + 1} in the old PDF.")
                match_found = True
                break

        if not match_found:
            print(f"Page {page_num + 1} in the new PDF has no match in the old PDF.")

    old_doc.close()
    new_doc.close()

# Example usage
old_pdf = "/Users/theinprem/Downloads/electron_v2.pdf"
new_pdf = "/Users/theinprem/Downloads/electron_v3.pdf"

compare_pdfs_with_hashing(old_pdf, new_pdf)