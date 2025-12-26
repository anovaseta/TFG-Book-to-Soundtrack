# Name: tags_summary.py
# Date: Oct 9, 2025
# Description: un script para, a partir de la 'bbdd' final de libros
# db_output_final.json, obtener un recuento de las tags obtenidas.
# Input: db_output_final.json con la información de los libros scrapeados
# Output: tags_summary.json con el recuento de las tags

import json

db = open("db_output_final.json", "r")
data = json.load(db)

tags = dict()
for key in data:
    for tag in data[key]["tags"]:
        if tag in tags:
            tags[tag] += 1
        else:
            tags[tag] = 1

tags = dict(sorted(tags.items(), key=lambda item: item[1], reverse=True))

for tag in tags:
    print(tag, ":", tags[tag])
db.close()

db = open("tags_summary.json", "w")
db.write(json.dumps(tags, indent=4))
db.close()
