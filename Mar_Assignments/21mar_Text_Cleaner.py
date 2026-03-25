import string
stopwords = ["is", "the", "am", "are", "and", "a", "an", "in", "on", "at", "to", "for"]
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    cleaned_words = [word for word in words if word not in stopwords]
    return " ".join(cleaned_words)
input_text = input("Enter a sentence: ")
output_text = clean_text(input_text)
print("\nCleaned Text:", output_text)