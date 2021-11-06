# Create unicode list by scraping HTML standards website

import requests
import json

UNICODE_LIST = 'https://html.spec.whatwg.org/entities.json'
UNICODE_FILE = './unicode-list'

json_file = requests.get(UNICODE_LIST).text
json_file = json.loads(json_file)

# clear contents of file
with open(UNICODE_FILE, 'w') as f:
    f.write("")

for symbol in json_file:
    character = json_file[symbol]['characters']

    # & is wacky in HTML
    if symbol[1:-1] == 'AM' or symbol[1:-1] == 'AMP':
        continue

    formatted = f'<span lang="{symbol[1:-1].lower()}"> {character} :{symbol[1:-1]}</span>'


    with open(UNICODE_FILE, 'a') as f:
        f.write(formatted + '\n')

