from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer

# Transforms text to array and remove punctuation
def tokenizeText(text):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(text)

# Delete empty words in spanish language
def clearEmptyWords(words):
    stop_words = set(stopwords.words('spanish'))
    filtered_sentence = []
    for word in words:
        if word not in stop_words:
            filtered_sentence.append(word)
    return list(filtered_sentence)

# Find all digits in an array
def findDigits(words):
    aux = []
    for word in words:
        if (word.isdigit()):
            aux.append(word)
    return aux
