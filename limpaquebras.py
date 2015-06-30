#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import nltk
from nltk.corpus import stopwords
from pyuca import Collator
c = Collator("corpustxt/allkeys.txt")
arq="corpustxt/catatau.txt"


fileObj = codecs.open( arq, "r", "utf-8" )
catatau = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

catatau = catatau.replace('\n', ' ').replace('\r', '')

print catatau

############# grava arquivo
file = codecs.open("corpustxt/catatau_semlinebreaks.txt", "w", "utf-8")
file.write(catatau)
file.close()
