import nltk

teks = open("doc.txt", "r")
x = teks.read()

tokens = nltk.tokenize.word_tokenize(x)
print(tokens)
