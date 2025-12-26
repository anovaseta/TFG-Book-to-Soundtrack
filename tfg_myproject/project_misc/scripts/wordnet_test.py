# Name: db_final.py
# Date: Nov 2025
# Description: un humilde script para probar funcionalidades de wordnet

import nltk

# nltk.download('wordnet')

from nltk.corpus import wordnet as wn

print(wn.synonyms('car'))
print(wn.synsets('thriller', pos=wn.NOUN))

# wordnet no me ha convencido
