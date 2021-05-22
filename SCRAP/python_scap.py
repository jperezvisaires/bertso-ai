#%% 

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from aux_scraping import eskuratu_doinuen_metadatuak
import numpy as np


import os
#%%



#%%


master_hiztegia = eskuratu_doinuen_metadatuak()
# Final number represents the first record to start showing from, there are currently 3162 doinu

#https://bdb.bertsozale.eus/web/doinutegia/emaitzak?bilatu=&izena=&hidden_izena=&mota=0&sortzailea=&hidden_sortzailea=&bertsolaria=&hidden_bertsolaria=&jasotzailea=&hidden_jasotzailea=&jasoa=&hidden_jasoa=&urtea=&kriterioak_gorde=1&per_page=3150

#%%

response = requests.get(doinutegia_page)

#%%

soup = BeautifulSoup(response.text, "html.parser")

#%% 

audio_files = soup.findAll('audio')

#%%

page_headers = soup.findAll('h4')

h4 = page_headers
# for each h4 



#%%

doinu_link = h4[1].find('a')
doinu_link  = doinu_link.get('href')

doinu_link

doinu_response = requests.get(doinu_link)

doinu_parsed = BeautifulSoup(doinu_response.text, "html.parser")

doinu_parsed.findAll('td')

#%%




#%% 

#def scrap_bertso_web


# inside td find the one with title "Midia eskuratu"
#%% 


#eskuratu_soinu_urlak(doinu_parsed)
_eskuratu_soinu_urlak('')

#%%


#%% 




for file_n in range(len(audio_files)):
    print(file_n)
    audio_file = audio_files[file_n]
    deskargatu_doinua(audio_file)


#map(deskargatu_doinua, audio_files)