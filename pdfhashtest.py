import hashlib
import pymupdf

def hashfile(file):

    # A arbitrary (but fixed) buffer size
    # 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536
    # Initializing the sha256() method
    sha256 = hashlib.sha256()
    # Opening the file provided as the first 
    # commandline argument
    with open(file, 'rb') as f:
        while True:
            # reading data = BUF_SIZE from the 
            # file and saving it in a variable
            data = f.read(BUF_SIZE)
            # True if eof = 1
            if not data:
                break
            # Passing that data to that sh256 hash 
            # function (updating the function with that data)
            sha256.update(data)

    # sha256.hexdigest() hashes all the input data passed
    # to the sha256() via sha256.update()
    # Acts as a finalize method, after which 
    # all the input data gets hashed
    # hexdigest() hashes the data, and returns 
    # the output in hexadecimal format
    return sha256.hexdigest()

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


def calculate_document_hash(pdf_path):
  """
  Calculates a document-level hash for a PDF file using PyMuPDF,
  considering page order.

  Args:
    pdf_path: Path to the PDF file.

  Returns:
    A hexadecimal string representing the document-level hash.
  """
  page_hashes = []
  doc = pymupdf.open(pdf_path)
  for page in doc:
    page_content = page.get_text().encode('utf-8')
    page_hash = hashlib.sha256(page_content).hexdigest() 
    page_hashes.append(page_hash)

  # Hash the array of page hashes
  page_hashes_str = ''.join(page_hashes).encode('utf-8')
  document_hash = hashlib.sha256(page_hashes_str).hexdigest()
  return document_hash

previous_hash_val = calculate_document_hash('/Users/theinprem/Downloads/electron_v2_notitle.pdf')
updated_hash_val = calculate_document_hash('/Users/theinprem/Downloads/electron_v3.pdf')
print(previous_hash_val);
print(updated_hash_val);
print(previous_hash_val == updated_hash_val);
# text_blocks = extract_text_blocks('/Users/theinprem/Downloads/electron_v3.pdf')
# print(len(text_blocks))
# for text in text_blocks:
# print(text)
# print(hash_val)