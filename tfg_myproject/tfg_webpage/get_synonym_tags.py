# Name: get_synonym_tags.py
# Date: Jan 11 2026
# Description: un script para obtener la lista de sinónimos de la bbdd
# Output: synonym_list.json con la lista

import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tfg_webpage.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from webapp.models import Synonym

django.setup()

if __name__ == '__main__':

    # get synonyms from db
    all_synonyms = [syn.synonym for syn in Synonym.objects.all()]

    # LastFM authentication credentials
    file_path = os.path.join("../", "project_misc/synonym_list.json")
    syn_file = open(file_path, "w")
    
    syn_file.write(json.dumps(all_synonyms, indent=4, ensure_ascii=False))

    syn_file.close()