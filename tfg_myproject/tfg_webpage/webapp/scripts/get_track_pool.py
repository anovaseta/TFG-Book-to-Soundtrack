# Name: initial_flow.py
# Date: Feb 02 2026
# Description: retratar un flujo inicial y rudimentario desde meter un libro (ISBN) hasta obtener una lista de canciones.

import os
import sys
import django
import json
import pylast
import random, secrets
import requests
import re

from .storygraph_scraper import book_info, book_search, add_weights_to_book
from webapp.models import Storygraph_Book, Storygraph_Tag, Tagged_Book, Synonym, Synonym_Relation, Spotify_Track, Spotify_Tag_Relation

def get_track_pool(book):
# returns the complete track pool of a certain book, stored in the database as is.

  synonyms = {}
  for t in book['tag_weights']:
    synonyms[t[0]] = {'weight': t[1], 'synonyms': {}}

  # print(synonyms)

  for t in synonyms.keys():
    # print(t)
    tag_id = Storygraph_Tag.objects.get(tag_name=t).id
    s_list = [Synonym.objects.get(id=sr.synonym_id).synonym for sr in Synonym_Relation.objects.filter(tag_id=tag_id)]
    # print(s_list)
    for s in s_list:
      synonyms[t]['synonyms'][s] = []

  # print(synonyms)

  for tag in synonyms.keys():
    for syn in synonyms[tag]['synonyms'].keys():
      # print(syn)
      syn_id = Synonym.objects.get(synonym=syn).id
      list_objects = [Spotify_Track.objects.get(id=rt.track_id) for rt in Spotify_Tag_Relation.objects.filter(tag_id=syn_id)]
      tracklist = [(t.name, t.artist, t.tag, t.spotify_json['external_urls']['spotify']) for t in list_objects]
      synonyms[tag]['synonyms'][syn] += tracklist

  #### useful for debug ######
  # n_tracks = 0
  # for tag in synonyms.keys():
  #   print(tag)
  #   # print(len(synonyms[tag]['synonyms'].items()))
  #   n_by_syn = 0
  #   for syn in synonyms[tag]['synonyms'].keys():
  #     n_by_syn += len(synonyms[tag]['synonyms'][syn])
  #     n_tracks += len(synonyms[tag]['synonyms'][syn])
  #   print(n_by_syn)

  return(synonyms)

  

  

  




    









