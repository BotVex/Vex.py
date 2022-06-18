import json

with open('animes.json', 'r') as f: 
  f = json.loads(f.read())

print(len(f)/40)
