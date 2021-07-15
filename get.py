# Create emoji list by scraping unicode website

import requests
import time

UNICODE_LIST = 'https://unicode.org/Public/emoji/13.1/emoji-test.txt'
EMOJI_FILE = './emoji-list'

txt = requests.get(UNICODE_LIST).text

with open(EMOJI_FILE, 'w') as f:
    f.write('')

# getting the emojis
for line in txt.split('\n'):
    if len(line) > 0 and line[0] == '#':
        pass
    else:
        s = line.split(';')
        if len(s) > 1:
            emoji_info = s[1].split('# ')[1].split()
            emoji_name = " ".join(emoji_info[2:]).replace(':', '')
            emoji_symbol = emoji_info[0]

            formatted = f'<span lang="{emoji_name.lower()}"> {emoji_symbol} :{emoji_name}</span>'

            with open(EMOJI_FILE, 'a') as f:
                f.write(formatted + '\n')
