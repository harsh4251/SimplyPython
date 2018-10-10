import nltk

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
snowball = nltk.stem.snowball.SnowballStemmer("english")

sentence2 = "When I was going into the woods I saw a bear lying asleep on the forest floor"
tokens2 = nltk.word_tokenize(sentence2)

print("\n",sentence2)
for stemmer in [porter, lancaster, snowball]:
    print([stemmer.stem(t) for t in tokens2])
