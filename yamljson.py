import yaml
import json
list = range(6)
list.append({'ipaddress':'192.168.0.1', 'snmpcommunity':'public'})
with open('w1_yaml.yml','w') as file:
   file.write(yaml.dump(list, default_flow_style=False))
