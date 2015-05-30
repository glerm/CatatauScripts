#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("allkeys.txt")




arq="catatau.txt"


fileObj = codecs.open( arq, "r", "utf-8" )
catatau = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(catatau) 


tokens = nltk.word_tokenize(catatau)

#catacorpus=nltk.Text(nltk.word_tokenize(catatau))


# ordenar
tokens.sort()



a = set(tokens)

glossario=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
glossario=sorted(glossario, key=c.sort_key)

glossario.reverse()

eu="Eu, contemporâneo do meu fantasma, olho-me no espelho e vejo nada. Que tal a fala, que tal você falando? Dizendo o que não sei, ouvindo o que estou cansado de saber? Quer ser eu? Crio contextos."

a=''
for x in xrange(3333):
	a=a+"\n\nEu, "+ random.choice(glossario)  +" do meu "+ random.choice(glossario) +", olho-me no "+ random.choice(glossario)  +" e vejo "+ random.choice(glossario)  +". "+"Isso pensa? "+"Isso "+random.choice(glossario)+"!  Quer ser "+random.choice(glossario)+"? Crio "+random.choice(glossario)+"."




txt=eu.decode('utf-8')+"\n\n"+a


############# grava arquivo
file = codecs.open("ContextoTaL.txt", "w", "utf-8")
file.write(txt)
file.close()
