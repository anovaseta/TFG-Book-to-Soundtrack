# Name: db_final.py
# Date: Sep 19, 2025
# Description: un script para unificar los datos en una única bbdd,
# eliminando duplicados.

import json

out1 = open("db_output_final.json", "r")
# out2 = open("db_output.json", "r")

db1 = json.load(out1)
# db2 = json.load(out2)

db_final = list()

for key in db1:
    if key not in db_final:
        db_final.append(key)
    else:
        print(key, "already there")

# for key in db2:
#     if key not in db_final:
#         db_final.append(key)
#         db1[key] = db2[key]
#     else:
#         print(key, "already there")

print("\nTotal books in final db:", len(db_final))
out1.close()

# out1 = open("db_output_final.json", "w")
# out1.write(json.dumps(db1, indent=4))
# out1.close()

# out2.close()
