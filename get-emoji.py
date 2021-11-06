# Create emoji list by scraping unicode website

import requests

def sanitize(string):
    new_string = ''
    for letter in string:
        if letter.isalpha() or letter == " ":
            new_string += letter
        else:
            new_string += '-'
    return new_string

UNICODE_LIST = 'https://unicode.org/Public/emoji/13.1/emoji-test.txt'
EMOJI_FILE = './emoji-list'

txt = requests.get(UNICODE_LIST).text

with open(EMOJI_FILE, 'w') as f:
    f.write('')

# getting the emojis
for line in txt.split('# subgroup: '):
    l = line.split('\n')

    # get emoji category
    emoji_category = l.pop(0)
    emoji_category.replace(':', '')

    for emoji in l:
        if not emoji or emoji[0] == "#":
            pass
        else:
            s = emoji.split(';')

            # get emoji details
            emoji_info = s[1].split('# ')[1].split()

            emoji_name = " ".join(emoji_info[2:]) \
                    .replace(':', '') \
                    .replace('&', 'and')

            emoji_symbol = emoji_info[0]

            formatted = f'<span lang="{emoji_name.lower()}-{sanitize(emoji_category.lower())}"> {emoji_symbol} :{emoji_name}</span>'
            with open(EMOJI_FILE, 'a') as f:
                f.write(formatted + '\n')
