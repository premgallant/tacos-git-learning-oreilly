import difflib
import re

def normalize_text(text):
  """Normalizes text by removing extra whitespace, newlines, 
  punctuation, and converting to lowercase.
  """
  text = text.lower()
  text = ' '.join(text.split())
  # text = re.sub(r'[\'.,;?`~!-–—()\[\]{}"“”\t\n ]+', '', text)  # Remove punctuation and multiple spaces
  # close to accuracy
  text = re.sub(r'[\t~!\':.,;`\[\]\n"“” ]', '', text)
  return text

def compare_strings(str1, str2):
  """Compares two strings for equality after normalization."""
  return normalize_text(str1) == normalize_text(str2)


def compare_paragraphs(text1, text2):
  """Compares two paragraphs using difflib's SequenceMatcher 
  with case-insensitive comparison and newline ignorance.
  """

  # Create a SequenceMatcher instance with a custom junk heuristic
  def isjunk(x):  
      return x in "\n.,;?`!-–—()[]{}'\"" "\t"  # Define characters to ignore

  sm = difflib.SequenceMatcher(isjunk=isjunk, 
                             a=normalize_text(text1), 
                             b=normalize_text(text2))
  # Calculate the similarity ratio
  ratio = sm.ratio()
  return ratio


# # Example usage
text1 = "The Office of Foreign Assets Control (OFAC) administers and enforces sanctions policy, based on Presidential declarations of “national emergency”.  OFAC has identified and listed numerous:"
text2 = "The Office of Foreign Assets Control (OFAC) administers and enforces sanctions policy,"
text_split = "based on Presidential declarations of “national emergency”.  OFAC has identified and listed numerous:"
text2 = text2+text_split

# text1 ="policy.                      You should read your policy and review your Declarations page for complete information on the"
# text2="   Policy. You should      read your policy and        review your          Declarations       page for complete information on the "

# text1="as “Specially Designated Nationals and Blocked              Persons”.This list can be located on the United States Treasury’s website - http://www.treas.gov/ofac. In accordance with OFAC regulations, if it is `determined that you or any other insured, or any person or entity claiming the benefits of this insurance has violated U.S. sanctions law or is a Specially Designated National and Blocked Person, as identified by OFAC, this insurance will be considered a blocked or frozen contract and all provisions of this insurance are immediately subject to OFAC. When an insurance policy is considered to be such a blocked or frozen contract, no payments nor premium refunds may be made without authorization from OFAC.  Other limitations on the premiums and payments also apply."
# text2="as “Specially Designated Nationals and Blocked Persons”.      This list can be located on the United States Treasury’s website - http//www.treas.gov/ofac. In accordance with OFAC regulations, if it is `determined that you or any other insured, or         any person or entity claiming the benefits of this insurance has violated U.S. sanctions law or is a Specially Designated National and Blocked Person, as identified by OFAC, this insurance will be considered a blocked or frozen contract and all provisions of this insurance are immediately subject to OFAC. When an insurance policy is considered to be such a blocked or frozen contract, no payments nor premium refunds may be made without authorization from OFAC.  Other limitations on the premiums and payments also apply."

#CHUBB PDF
# text1= "M. If there is “underlying insurance”, or “other insurance” applicable to a “loss” subject to a “scheduled retained"
# text2="M. If there is “underlying insurance”, or “other insurance”            applicable to a “loss” subject to a “scheduled retained...."
# text3 = text2+text_split;
print(text2)
print(text1)
ratio = compare_paragraphs(text1, text2)
print(f"Similarity ratio: {ratio}")
print(compare_strings(text1, text2))