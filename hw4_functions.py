import re

def normalize_text(text):
    return text.lower()

def create_sentence_from_last_words(text):
    sentences = text.split('.')
    last_words = [sentence.split()[-1] for sentence in sentences if sentence.split()]
    return ' '.join(last_words) + '.'

def add_sentence_to_text(text, sentence):
    return text + ' ' + sentence

def fix_misspelling(text):
    return re.sub(r'\biz\b', 'is', text)

def count_whitespaces(text):
    return text.count(' ')

def main():
    # Copy the text to a variable
    text = """homEwork:
    tHis iz your homeWork, copy these Text to variable.
    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    normalized_text = normalize_text(text)
    new_sentence = create_sentence_from_last_words(normalized_text)
    text_with_new_sentence = add_sentence_to_text(normalized_text, new_sentence)
    corrected_text = fix_misspelling(text_with_new_sentence)
    num_whitespaces = count_whitespaces(corrected_text)

    print(f"Corrected text: {corrected_text}")
    print(f"Number of whitespaces: {num_whitespaces}")

if __name__ == "__main__":
    main()