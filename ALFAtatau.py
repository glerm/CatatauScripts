#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")


# arquivo analisado (no mesmo diretorio)
arq="corpustxt/catatau_semlinebreaks.txt"
fileObj = codecs.open( arq, "r", "utf-8" )
mikrofesto = fileObj.read() 

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')
catalinhas=stok.tokenize(mikrofesto) 



#separando pontuações do final de palavras e demais tokens
tokens = nltk.word_tokenize(mikrofesto)

# limpando conectivos
#cleanupDoc(tokens)

#formatando em estrutura de dados nltk para padronizar posteriormente
catacorpus=nltk.Text(nltk.word_tokenize(mikrofesto))


#convertendo para vetor para filtrar repitições
a = set(tokens)
# retornando para tipo lista
glossario=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos
glossario=sorted(glossario, key=c.sort_key)

# ordenado pelo reverso pra ficar de a até z
glossario.reverse()

# formatando separado por espaços e vírgulas
a=""
for w in glossario:
	a=w+", "+a

print a

############# grava arquivo
#file = codecs.open("AquiloLexico.txt", "w", "utf-8")
#file.write(a)
#file.close()
