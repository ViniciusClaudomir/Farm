import json
with open('config.json','r') as arq:
    LOAD_CONFIG = json.loads(arq.read())
