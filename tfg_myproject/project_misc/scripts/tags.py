# Name: tags_summary.py
# Date: Oct 9, 2025
# Description: varias funciones relacionadas con tags
# Input: db_output_final.json con la información de los libros scrapeados
# Output: tags_summary.json con el recuento de las tags

import json

def tag_recount():
    # a partir de la 'bbdd' final de libros
    # db_output_final.json, obtener un recuento de las tags obtenidas
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


def tag_reload():
    # ampliar lista de tags, bajar el listón de 50 a ??

    f = open("json_files/all_books_extended.json", 'r+')
    all_books_extended = json.loads(f.read())
    print(len(all_books_extended))
    for b in all_books_extended.values():
        extended_tags = []
        total = 0
        weighted_tags = []
        try: 
            # print('-----------------------------------------------')
            # print(b['title'])
            # tags = b['tags']
            tag_percentage = b['tag_percent']
            # print(tag_percentage)
            for t, p in b['tag_percent'].items():
                if int(p) > 25:
                    total += int(p)
                    extended_tags.append((t,p))
            # print(extended_tags)
            for t, p in extended_tags:
                weighted_tags.append((t,float(int(p)/total)))
            # print(weighted_tags) 
            b['tag_weights'] = weighted_tags
        except Exception as e:
            print(e)
    f.write(json.dumps(all_books_extended, indent=4))
    f.close()



if __name__ == '__main__':
    # tag_recount()
    tag_reload()

