import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

teks = open("alice.txt", "r") 
t = teks.read()

tokenisasi = tokenizer.tokenize(t)
print(tokenisasi)