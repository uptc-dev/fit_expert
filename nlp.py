from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer

gender_synonym = [
'mujer',
'hombre',
'chica',
'chico',
'niña',
'niño',
'hembra',
'fémina',
'dama',
'señora',
'señorita',
'doncella',
'joven',
'muchacha',
'moza',
'chica',
'esposa',
'señora',
'compañera',
'consorte',
'desposada',
'criatura',
'individuo',
'ser',
'ente',
'humano',
'semejante',
'prójimo',
'sujeto',
'varón',
'masculino',
'macho',
'mortal',
'persona',
'marido',
'esposo',
'amante',
'compañero',
]

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

# Determinate gender
def findGender(words):
    gender = ''
    for word in words:
        if word in gender_synonym:
            gender = word
    return gender

# Determinate if a sentence is affirmative or negative
def moodSentence(words):
    pos = 0
    neg = 0
    for word in words:
        if (isWordAffirmative(word)):
            print('pos' + word)
            pos = pos + 1
        elif (isWordNegative(word)):
            print('neg' + word)
            neg = neg + 1
    print('Positive ' + pos)
    print('Negative ' + neg)

# Returns if a word is affirmative or not
def isWordAffirmative(word):
	listAfirmative = ['mí','mís','mi','mis','afirmativamente','evidentemente','sí','si','claro','talves','talvez','tal','supuesto','obvio','efectivamente','duda','correctamente','acuerdo', 'muy', 'bien', 'genial']
	return True if word in listAfirmative else False

# Returns if a word is negative or not
def isWordNegative(word):
	listNegative = ['negativamente','nunca','jamás','jamas','no','ningún','ningun','desacuerdo','jamaz','tampoco']
	return True if word in listNegative else False
