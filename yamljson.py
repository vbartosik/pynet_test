import yaml
import json
data = range(6)
data.append({'ipaddress':'192.168.0.1', 'snmpcommunity':'public'})
with open('w1_yaml.yml','w') as f:
   f.write(yaml.dump(data, default_flow_style=False))
with open('w1_json.json','w') as f:
   json.dump(data, f)
