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
import math

from .storygraph_scraper import book_info, book_search, add_weights_to_book
from webapp.models import Storygraph_Book, Storygraph_Tag, Tagged_Book, Synonym, Synonym_Relation, Spotify_Track, Spotify_Tag_Relation

def get_track_pool(book, n_tracks):
# returns the complete track pool of a certain book, stored in the database as is.

  print(book)

  # calculates the number of tracks per tag (based on total number of tracks)
  tag_tracks = [(t[0], float(n_tracks)*t[1]) for t in book['tag_weights']]
  # print(tag_tracks)
  tag_residual = [[t[0], t[1]-math.floor(t[1]), int(t[1]-(t[1]-math.floor(t[1])))] for t in tag_tracks]
  # print(tag_residual)

  sum_tracks = 0
  for t in tag_residual:
    sum_tracks += t[2]
  dif_tracks = int(n_tracks) - sum_tracks
  # print(dif_tracks)

  if dif_tracks > 0:
    tag_residual.sort(key=lambda t: t[1], reverse=True)
    # print(tag_residual)
    i = 0
    while dif_tracks > 0:
      dif_tracks -= 1
      tag_residual[i][2] += 1
      i += 1
    # print(tag_residual)

  sum_tracks = 0
  for t in tag_residual:
    sum_tracks += t[2]
  if sum_tracks == int(n_tracks):
    print('Check!')
  else:
    print('Something is wrong')

  synonyms = {}
  synonyms_two = {}
  for t in tag_residual:
    synonyms[t[0]] = {'n_tracks': t[2], 'synonyms': {}}
    synonyms_two[t[0]] = {'n_tracks': t[2], 'tracks': []}

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
      tracklist = []
      for t in list_objects:
        if t.spotify_json['album']['images'] == []:
          tracklist.append((t.name, t.artist, t.tag, t.spotify_json['uri'],t.spotify_json['external_urls']['spotify']))
        else:
          tracklist.append(((t.name, t.artist, t.tag, t.spotify_json['uri'],t.spotify_json['external_urls']['spotify'], t.spotify_json['album']['images'][0]['url'])))
      # tracklist = [(t.name, t.artist, t.tag, t.spotify_json['uri'],t.spotify_json['external_urls']['spotify'], t.spotify_json['album']['images'][0]['url']) for t in list_objects]
      synonyms[tag]['synonyms'][syn] += tracklist
      synonyms_two[tag]['tracks'] += tracklist

  #### useful for debug ######
  n_tracks = 0
  for tag in synonyms.keys():
    print(tag)
    print(len(synonyms[tag]['synonyms'].items()))
    n_by_syn = 0
    for syn in synonyms[tag]['synonyms'].keys():
      n_by_syn += len(synonyms[tag]['synonyms'][syn])
      n_tracks += len(synonyms[tag]['synonyms'][syn])
    print(n_by_syn)

  return([n_tracks, synonyms_two, synonyms])
