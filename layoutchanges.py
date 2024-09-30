import hashlib
import pymupdf

def extract_text_blocks_page(pdf_path,page_number):
    """
    Extracts text blocks from a PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: A list of text blocks, where each block is a string.
    """

    doc = pymupdf.open(pdf_path)
    text_blocks = []
    page = doc[page_number]  # Get the desired page
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

def calculate_document_hashes(pdf_path):
  """
  Calculates page-level and paragraph-level hashes for a PDF.

  Args:
    pdf_path: Path to the PDF file.

  Returns:
    A tuple containing two dictionaries:
      - page_hash_map: {page_hash: page_number}
      - paragraph_hash_map: {paragraph_hash: page_hash}
  """
  page_hash_map = {}
  paragraph_hash_map = {}
  doc = pymupdf.open(pdf_path)
  for page_num, page in enumerate(doc):
    page_content = page.get_text().encode('utf-8')
    page_hash = hashlib.sha256(page_content).hexdigest()
    page_hash_map[page_hash] = page_num + 1  # Page numbers start from 1

    # Extract paragraphs (this might need adjustment)
    # paragraphs = page_content.decode('utf-8').split("\n\n") 
    paragraphs = extract_text_blocks_page(pdf_path,page_num) 
    for paragraph in paragraphs:
      paragraph_hash = hashlib.sha256(paragraph.encode('utf-8')).hexdigest()
      paragraph_hash_map[paragraph_hash] = page_hash
  return page_hash_map, paragraph_hash_map


# Example usage
pdf_path1 = "/Users/theinprem/Downloads/electron_v2.pdf"
pdf_path2 = "/Users/theinprem/Downloads/electron_v2_heading_change.pdf"

doc_version1_map, page_para_content_hash_version1map = calculate_document_hashes(pdf_path1)
print(doc_version1_map)
print(page_para_content_hash_version1map)
# doc_version2_map, page_para_content_hash_version2map = calculate_document_hashes(pdf_path2)

# for page_hash, page_num_v2 in doc_version2_map.items():
#   if page_hash in doc_version1_map:
#     page_num_v1 = doc_version1_map[page_hash]
#     if page_num_v1 == page_num_v2:
#       print(f"Page {page_num_v2} is identical in content and position.")
#     else:
#       print(f"Page {page_num_v2} (originally page {page_num_v1}) has been rearranged.")
#   else:
#     # Check for moved paragraphs
#     found_moved_paragraph = False
#     for paragraph_hash in page_para_content_hash_version2map:
#       if paragraph_hash in page_para_content_hash_version1map:
#         original_page_hash = page_para_content_hash_version1map[paragraph_hash]
#         original_page_num = doc_version1_map.get(original_page_hash)
#         print(f"  - Paragraph from original page {original_page_num} moved to page {page_num_v2}")
#         found_moved_paragraph = True 

#     # If no moved paragraphs were found, it indicates new content
#     if not found_moved_paragraph:  
#         print(f"Page {page_num_v2} has new content.")