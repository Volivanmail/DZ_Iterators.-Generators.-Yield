import json
from pprint import pprint

with open('countries.json', encoding='utf-8') as f:
    file = json.load(f)
    print(len(file))

class CountryIterator:

    def __init__(self, file):
        self.file = file
        self.cursor = None
        self.URL = "https://ru.wikipedia.org/wiki/"

    def __iter__(self):
        self.cursor = -1
        return self

    def get_obj(self):
        name = file[self.cursor]['name']['common']
        rus_name = file[self.cursor]['translations']['rus']['common']
        Country_dict[name] = self.URL + rus_name
        Country = {name: self.URL + rus_name}
        return Country


    def __next__(self):
        self.cursor += 1
        if self.cursor == len(file):
            raise StopIteration
        return self.get_obj()

Country_dict = {}

for Country in CountryIterator(file):
    pprint(Country)

print(len(Country_dict))
pprint(Country_dict)

with open('countries_new.json', 'w', encoding='utf-8') as f:
    json.dump(Country_dict, f, ensure_ascii=False, indent=1)