import random

from nltk import NaiveBayesClassifier as nbc
from nltk import chunk

from nltk.corpus import stopwords
from nltk.corpus import names

from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

from nltk.tag import pos_tag

from nameparser.parser import HumanName

class NaturalLanguageProcessing(object):
    """docstring for Nlp."""
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        # List of examples and corresponding class labels.
        self.labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
        random.shuffle(self.labeled_names)

        featuresets = [(self.gender_features(n), gender) for (n, gender) in self.labeled_names]
        self.classifier = self.train_gender(featuresets[1000:])

        # print(self.classifier.classify(self.gender_features('Ramon')))

    # Transforms text to array and remove punctuation
    def tokenize_text(self, text):
        # text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        return tokenizer.tokenize(text)

    # Delete empty words in spanish language
    def clear_empty_words(self, words):
        filtered_sentence = []
        for word in words:
            if word.lower() not in self.stop_words:
                filtered_sentence.append(word)
        return list(filtered_sentence)

    # Find human names in a text, text must be tokenized
    def find_human_names(self, words):
        pos = pos_tag(words)
        sentt = chunk.ne_chunk(pos, binary = False)
        person_list = []
        person = []
        name = ""
        for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
            for leaf in subtree.leaves():
                person.append(leaf[0])
            if len(person) > 1: #avoid grabbing lone surnames
                for part in person:
                    name += part + ' '
                if name[:-1] not in person_list:
                    person_list.append(name[:-1])
                name = ''
            person = []
        return person_list

    # Find all digits in an array
    def find_digits(self, words):
        aux = []
        for word in words:
            if (word.isdigit()):
                aux.append(word)
        return aux

    # Define features to evaluate names
    def gender_features(self, name):
        return {'last_letter': name[-1]}

    def train_gender(self, train_set):
        return nbc.train(train_set)

    # Get all stop word
    def get_stop_words(self):
        return self.stop_words




sentence = "an They My name is michael Francisco L and I'm 23 years old"
nlp = NaturalLanguageProcessing()
names = nlp.find_human_names(nlp.tokenize_text(sentence))
print(names)

# print(nlp.get_stop_words())
# print('\n')

# sentence = "an They My name is michael Francisco Barrera and I'm 23 years old"
# # print(sentence)
# # print('\n')
# sentence = nlp.tokenize_text(sentence)
# print(sentence)
# print('\n')
# sentence = nlp.clear_empty_words(sentence)
# print(sentence)
# print('\n')
# sentence = nlp.find_proper_nouns(sentence)

# print('Gender features---------')
# name = 'Francisco'
# print('Name: ' + name)
# print(nlp.gender_features(name))
#
# labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
# import random
# import nltk
# # random.shuffle(labeled_names)
# featuresets = [(nlp.gender_features(n), gender) for (n, gender) in labeled_names]
# train_set = featuresets[1000:]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(classifier.classify(nlp.gender_features('Katherine')))

# qry = "who is Mahatma Gandhi"
# tokens = nltk.tokenize.word_tokenize(qry)
# pos = nltk.pos_tag(tokens)
# sentt = nltk.ne_chunk(pos, binary = False)
# print(sentt)
# # for word in sentt:
# #     print(word)
# person = []
# for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
#     for leave in subtree.leaves():
#         person.append(leave)
# print ("person=", person)






# names = get_human_names(text)
# print("LAST, FIRST")
# for name in names:
#     last_first = HumanName(name).last + ', ' + HumanName(name).first
#     print(last_first)
