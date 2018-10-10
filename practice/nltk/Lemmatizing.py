import nltk

sentence2 = "When I was going into the woods I have seen a bear lying asleep on the forest ceiling"
tokens2 = nltk.word_tokenize(sentence2)
wnl = nltk.WordNetLemmatizer()
tokens2_pos = nltk.pos_tag(tokens2)  #nltk.download("averaged_perceptron_tagger")

print(sentence2)
print([wnl.lemmatize(t) for t in tokens2])
