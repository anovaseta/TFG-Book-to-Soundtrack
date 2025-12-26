# Name: tag_types.py
# Date: Dec 23 2025
# Description: un script para emparejar a cada etiqueta con su 'tipo'


import json
import os
# import sys
# sys.path.append('\\wsl.localhost\Ubuntu\home\manuloseta\TFG\tfg_myproject\project_misc')
# import project_misc.scripts

# f_path = r'\\wsl.localhost\Ubuntu\home\manuloseta\TFG\tfg_myproject\project_misc\tags_classification.json'

f_path = os.path.join('./', 'tags_classification.json')
db = open(f_path, "r+")  # incomplete classification of tags
data = json.load(db)

# f2_path = r"\\wsl.localhost\Ubuntu\home\manuloseta\TFG\tfg_myproject\project_misc\tags_summary.json"

f2_path = os.path.join('./', 'tags_summary.json')
db_2 = open(f2_path, "r")  # all the tags in the current db
data2 = json.load(db_2)

all_tags = data2.keys()
# print(all_tags)

# syphon all unclassified tags into 'other'
for tag in all_tags:
    if tag not in data["mood"]:
        if tag not in data["pace"]:
            if tag not in data["genre"]:
                if tag not in data["other"]:
                    print(tag, " not in file")

# db.write(json.dumps(data))

db.close()
db_2.close()
