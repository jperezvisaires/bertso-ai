#%% 

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import os
#%%

doinutegia_page = 'https://bdb.bertsozale.eus/web/doinutegia/emaitzak?bilatu=&izena=&hidden_izena=&mota=0&sortzailea=&hidden_sortzailea=&bertsolaria=&hidden_bertsolaria=&jasotzailea=&hidden_jasotzailea=&jasoa=&hidden_jasoa=&urtea=&kriterioak_gorde=1'

# Final number represents the first record to start showing from, there are currently 3162 doinu

#https://bdb.bertsozale.eus/web/doinutegia/emaitzak?bilatu=&izena=&hidden_izena=&mota=0&sortzailea=&hidden_sortzailea=&bertsolaria=&hidden_bertsolaria=&jasotzailea=&hidden_jasotzailea=&jasoa=&hidden_jasoa=&urtea=&kriterioak_gorde=1&per_page=3150

#%%

response = requests.get(doinutegia_page)
print(response)

#%%

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

#%% 

h4 = soup.findAll('h4')
doinu_link = h4[1].find('a')
doinu_link = doinu_link.get('href')

doinu_response = requests.get(doinu_link)
doinu_parsed = BeautifulSoup(doinu_response.text, "html.parser")
dd = doinu_parsed.findAll('dd')
title = dd[0].string
print(title)

dl_horizontal = doinu_parsed.findAll('dl', ["dl-horizontal"])
for span in dl_horizontal[-1].find_all('span'):
    print(span.string)


#%%

def sortu_patha(doinuaren_urla):
    import re

    current_dir = os.getcwd()

    audio_ref_zenbakia = re.search( 'mp3a/[0-9]*', doinuaren_urla)

    audio_ref_zenbakia = audio_ref_zenbakia.group(0)

    audio_ref_zenbakia = re.sub( pattern = 'mp3a/',string = audio_ref_zenbakia, repl = '')

    return os.path.join(current_dir, audio_ref_zenbakia + '.mp3')


def deskargatu_doinua(audio_file):

    doinuaren_urla = audio_file['src']
    urllib.request.urlretrieve( doinuaren_urla, sortu_patha(doinuaren_urla) )

#%% 

for file_n in range(len(audio_files)):
    print(file_n)
    audio_file = audio_files[file_n]
    deskargatu_doinua(audio_file)


#map(deskargatu_doinua, audio_files)