import re

# Copy the text to a variable
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.
  
  
  
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Normalize the text
normalized_text = text.lower()

# Create a sentence with the last words of each existing sentence
sentences = normalized_text.split('.')
last_words = [sentence.split()[-1] for sentence in sentences if sentence.split()]
new_sentence = ' '.join(last_words) + '.'

# Add the new sentence to the end of the paragraph
normalized_text += ' ' + new_sentence

# Fix the misspelling of "iz" to "is"
corrected_text = re.sub(r'\biz\b', 'is', normalized_text)

# Calculate the number of whitespace characters
num_whitespaces = corrected_text.count(' ')

print(f"Corrected text: {corrected_text}")
print(f"Number of whitespaces: {num_whitespaces}")