#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")
arq="corpustxt/catatau_semlinebreaks.txt"


fileObj = codecs.open( arq, "r", "utf-8" )
catatau = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(catatau) 


#limpa palavras conectivas
def cleanupDoc(s):
     stopset = set(stopwords.words('portuguese'))
     tokens = nltk.word_tokenize(s)
     cleanup = " ".join(filter(lambda word: word not in stopset, s.split()))
     return cleanup





tokens = nltk.word_tokenize(catatau)

catacorpus=nltk.Text(nltk.word_tokenize(catatau))


# ordenar
#tokens.sort()



a = set(tokens)

glossario=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
glossario=sorted(glossario, key=c.sort_key)

glossario.reverse()

a=""

for w in glossario:
	a=w+", "+a


print catacorpus.dispersion_plot(["nada", "tudo", "monstro", "Occam","mundo","perdido","fim"])


############# grava arquivo
#file = codecs.open("Alfatatau.txt", "w", "utf-8")
#file.write(a)
#file.close()
