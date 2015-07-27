#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")


# arquivo analisado (no mesmo diretorio)
arq="corpustxt/iliada/BUTLER_ILIAD.txt"
fileObj = codecs.open( arq, "r", "utf-8" )
iliada = fileObj.read() 

# separa em linhas
stok = nltk.data.load('tokenizers/punkt/english.pickle')
catalinhas=stok.tokenize(iliada) 



#separando pontuações do final de palavras e demais tokens
tokens = nltk.word_tokenize(iliada)

# limpando conectivos
#cleanupDoc(tokens)

#formatando em estrutura de dados nltk para padronizar posteriormente
catacorpus=nltk.Text(nltk.word_tokenize(iliada))


#convertendo para vetor para filtrar repetições
a = set(tokens)
# retornando para tipo lista - LEXICO DA ILIADA EM FORMATO LISTA
#lex_ILIADA=list(a)

# usando o padrao de ordenamento do collate pyuca para considerar acentos - ORDENANDO
#lex_ILIADA=sorted(lex_ILIADA, key=c.sort_key)

#importar corpus da biblia do rei james
lex_BIBLE=nltk.corpus.gutenberg.words('bible-kjv.txt')

#convertendo para vetor para filtrar repetições
b=set(lex_BIBLE)

# retornando para tipo lista - LEXICO DA BIBLIA EM FORMATO LISTA
#lex_BIBLE=list(b)

# usando o padrao de ordenamento do collate pyuca para considerar acentos - ORDENANDO
#lex_BIBLE=sorted(lex_BIBLE, key=c.sort_key)

#o que tem na iliada fora o que tem na biblia
ILIAD_not_BIBLE = a - b
# convertendo pra lista e ordenando (considerando acentos)
ILIAD_not_BIBLE=list(ILIAD_not_BIBLE)
ILIAD_not_BIBLE=sorted(ILIAD_not_BIBLE, key=c.sort_key)
# formatando separado por espaços e vírgulas
ILIAD_not_BIBLE.reverse() #inverter pois a iteração é reversa
X=""
for w in ILIAD_not_BIBLE:
	X=w+", "+X

#o que tem na biblia fora o que tem na biblia
BIBLE_not_ILIAD = b - a
# convertendo pra lista e ordenando (considerando acentos)
BIBLE_not_ILIAD=list(BIBLE_not_ILIAD)
BIBLE_not_ILIAD=sorted(BIBLE_not_ILIAD, key=c.sort_key)
# formatando separado por espaços e vírgulas
BIBLE_not_ILIAD.reverse() #inverter pois a iteração é reversa
Y=""
for w in BIBLE_not_ILIAD:
	Y=w+", "+Y



# o que os dois livros tem de lexico comum
BIBLIADA = a & b
# convertendo pra lista e ordenando (considerando acentos)
BIBLIADA=list(BIBLIADA)
BIBLIADA=sorted(BIBLIADA, key=c.sort_key)
# formatando separado por espaços e vírgulas
BIBLIADA.reverse() #inverter pois a iteração é reversa
Z=""
for w in BIBLIADA:
	Z=w+", "+Z



#juntando os tres em um txt
XYZ="ILIAD NOT BIBLE \n\n\n\n ---\n\n\n"+X+"BIBLE NOT ILIAD \n\n\n\n ---\n\n\n"+Y+"BIBLIAD \n\n --------------\n"+Z



############# grava arquivo
file = codecs.open("BIBLIADA.txt", "w", "utf-8")
file.write(XYZ)
file.close()







