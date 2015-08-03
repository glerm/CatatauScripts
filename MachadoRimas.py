#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")



#importar corpus da biblia do rei james
M=nltk.corpus.machado.words()

#convertendo tudo pra minuscula
M=[x.lower() for x in M]

#convertendo para vetor para filtrar repetições
M=set(M)

# retornando para tipo lista - LEXICO DA BIBLIA EM FORMATO LISTA
M=list(M)


# usando o padrao de ordenamento do collate pyuca para considerar acentos - ORDENANDO
M=sorted(M, key=c.sort_key)


# convertendo pra lista e ordenando (considerando acentos)
M=list(M)
M=sorted(M, key=c.sort_key)
# formatando separado por espaços e vírgulas
M.reverse() #inverter pois a iteração é reversa



TXT=""
count=0
for w in M:
	m = re.match("^.*"+sys.argv[1]+"$", w, re.MULTILINE)
	if m:
		TXT=w+", "+TXT
		count=count+1
		print w + " -  "+str(count)
	

############# grava arquivo
#file = codecs.open("MACHADORIMAS.txt", "w", "utf-8")
#file.write(TXT)
#file.close()







