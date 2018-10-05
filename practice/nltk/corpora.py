import nltk
nltk.download("reuters")
nltk.download('punkt')   # Punkt Tokenizer Model
nltk.download('averaged_perceptron_tagger')  # Part-of-Speech Tokeniser
nltk.download("stopwords") # Stopwords

#Categories, Files and Words

from nltk.corpus import reuters
categories = reuters.categories()
print("Number of Categories:",len(categories))
print(categories[0:9],categories[-10:])


#Individual words can be extracted with the words() method:

words = reuters.words()
print("number of words", len(words) )
print("first 10 words:", words[0:9])


#Extract at a sepecific category
tradeWords = reuters.words(categories = 'trade')
len(tradeWords)

#Remove Stopwords and Punctuation
from nltk.corpus import stopwords
import string
print(stopwords.words('english'))

# This takes a couple of minutes to run
tradeWords = [w for w in tradeWords if w.lower() not in stopwords.words('english') ]

tradeWords = [w for w in tradeWords if w not in string.punctuation]
punctCombo = [c+"\"" for c in string.punctuation ]+ ["\""+c for c in string.punctuation ]
tradeWords = [w for w in tradeWords if w not in punctCombo]
len(tradeWords)


#Word Frequency Distribution
fdist = nltk.FreqDist(tradeWords)
fdist.plot(20, cumulative=False)


for word, frequency in fdist.most_common(10):
	print(word, frequency)


#Bi-Grams
biTradeWords = nltk.bigrams(tradeWords)
biFdist = nltk.FreqDist(biTradeWords)
biFdist.plot(20, cumulative=False)


#Exploring the Penn Treebank
nltk.download('treebank')
from nltk.corpus import treebank
words = treebank.words()
tagged = treebank.tagged_words()
print(type(tagged))
print("Word Count", len(words))
print("Tagged words sample: ",tagged[0:9])


parsed = treebank.parsed_sents()[0]
print(parsed)
type(parsed)

import IPython
IPython.core.display.display(parsed)
