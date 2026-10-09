from texttools.cleaning import clean_text
from texttools.tokenization import tokenize_words, tokenize_sentences
from texttools.frequency import word_frequency

sample_text = "Python is powerful, and Python is easy to learn! Welcome to Python."
cleaned = clean_text(sample_text)
words = tokenize_words(cleaned)
sentences = tokenize_sentences(sample_text)
freq = word_frequency(words)

print("Original Text:", sample_text)
print("Cleaned Text:", cleaned)
print("Tokens:", words)
print("Word Frequency:", freq)
