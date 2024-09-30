import pymupdf
import hashlib


def extract_page_text(pdf_path, page_number):
  """
  Extracts all text from a single page of a PDF using pymupdf.

  Args:
      pdf_path (str): Path to the PDF file.
      page_number (int): The page number to extract (0-indexed).

  Returns:
      str: The extracted text from the page.
  """

  doc = pymupdf.open(pdf_path)
  page = doc[page_number]  # Get the desired page
  text = page.get_text()  # Extract the text
  doc.close()
  return text

def extract_text_blocks(pdf_path):
    """
    Extracts text blocks from a PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: A list of text blocks, where each block is a string.
    """

    doc = pymupdf.open(pdf_path)
    text_blocks = []
    for page in doc:
        print(page)
        blocks = page.get_text("blocks")
        current_block = ""
        for x0, y0, x1, y1, text, block_num, block_type in blocks:
            if block_type == 0:  # Text block
                if len(current_block) > 0 and y0 - prev_y1 > 10:  # Adjust threshold as needed
                    text_blocks.append(current_block.strip())
                    current_block = ""
                current_block += text
                prev_y1 = y1
        if current_block:
            text_blocks.append(current_block.strip())  # Add the last block
    doc.close()
    return text_blocks

def compare_pdfs_with_block_hashing(old_pdf_path, new_pdf_path):
    """
    Compares two PDFs with potential paragraph movements using block-level hashing.

    Args:
        old_pdf_path (str): Path to the older PDF file.
        new_pdf_path (str): Path to the newer PDF file.
    """

    old_doc = pymupdf.open(old_pdf_path)
    new_doc = pymupdf.open(new_pdf_path)

    old_block_hashes = {}
    for page_num in range(old_doc.page_count):
        page_text = extract_page_text(old_pdf_path,page_num)
        print("**************")
        print(page_text)
        print("*************")
        blocks = extract_text_blocks(old_pdf_path)
        for block in blocks:
            block_hash = hashlib.sha1(block.encode()).hexdigest()
            old_block_hashes[block_hash] = block  # Store the block itself

    for page_num in range(new_doc.page_count):
        new_blocks = extract_text_blocks(new_pdf_path)
        for new_block in new_blocks:
            new_block_hash = hashlib.sha1(new_block.encode()).hexdigest()
            if new_block_hash in old_block_hashes:
                print(f"Block '{new_block}' found in both PDFs.")
            else:
                print("================================================")
                print(f"Block '{new_block}' is new in the updated PDF.")

    old_doc.close()
    new_doc.close()

# Example usage
old_pdf = "/Users/theinprem/Downloads/electron_v3.pdf"
new_pdf = "/Users/theinprem/Downloads/electron_v2_heading_change.pdf"

# compare_pdfs_with_block_hashing(old_pdf, new_pdf)
