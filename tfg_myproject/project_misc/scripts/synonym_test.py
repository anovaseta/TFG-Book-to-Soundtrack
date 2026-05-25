# Name: synonym_test.py
# Date: Nov 2025
# Description: un humilde script para probar distintas librerías de sinónimos

# import nltk
from PyMultiDictionary import MultiDictionary

dict = MultiDictionary()

# terms = ["emotional", "reflective", "adventurous", "dark", "mysterious", "sad", "funny", "lighthearted", 
#          "challenging", "tense", "inspiring", "hopeful", "relaxing"]
terms = ["dark"]

for term in terms:
    print("-----------------------------------------")
    syn_list = dict.synonym('en', term)
    syn_list.sort()
    print(term, " ------>", syn_list)
