import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

teks = "Kata kata yang ingin di token disasi"
tokenisasi = tokenizer.tokenize(teks)
print(tokenisasi)