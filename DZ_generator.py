import hashlib
import json
from pprint import pprint

with open('countries_new.json', encoding='utf-8') as f:
    file = json.load(f)

print(len(file))

def gen_md5 (path):
    for country in path.values():
        hash_object = hashlib.md5(country.encode())
        yield hash_object.hexdigest()

x = 0
for country in gen_md5(file):
    print(country)
    x += 1
print(x)
