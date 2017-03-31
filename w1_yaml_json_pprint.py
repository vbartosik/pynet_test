import yaml
import json
from pprint import pprint as pp

with open('w1_yaml.yml') as f:
    pp(yaml.load(f))
with open('w1_json.json') as f:
    pp(json.load(f))

