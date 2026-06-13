from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os


def write_json(path, payload):
  with open(path, 'w') as outfile:
    json.dump(payload, outfile, ensure_ascii=False)

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
write_json('results/gs_data.json', author)
write_json('results/gs_data_shieldsio.json', shieldio_data)
