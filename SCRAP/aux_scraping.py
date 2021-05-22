# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:47:38 2021

@author: kerma
"""
import urllib
import os
from bs4 import BeautifulSoup
import requests
import urllib.request
import time

def eskuratu_doinuen_metadatuak():
    
    numbering_urls = list(range(0,3162, 50))

    base_doinu_url = 'https://bdb.bertsozale.eus/web/doinutegia/emaitzak?bilatu=&izena=&hidden_izena=&mota=0&sortzailea=&hidden_sortzailea=&bertsolaria=&hidden_bertsolaria=&jasotzailea=&hidden_jasotzailea=&jasoa=&hidden_jasoa=&urtea=&kriterioak_gorde=51&per_page='
    
    
    master_doinutegi_hiztegia = []
    
    for url_number in numbering_urls:
        
        doinutegia_page = base_doinu_url + str(url_number)
        
        print('url number is:', url_number)
        time.sleep(2)
        
        response = requests.get(doinutegia_page)

        soup = BeautifulSoup(response.text, "html.parser")
        
        page_headers = soup.findAll('h4')
        
        doinu_hiztegia = list(map(eskuratu_doinu_urlko_soinulinkak, page_headers))
        
        master_doinutegi_hiztegia.append(doinu_hiztegia)

    return master_doinutegi_hiztegia





def sortu_patha(doinuaren_urla):
    import re

    current_dir = os.getcwd()

    audio_ref_zenbakia = re.search('mp3a/[0-9]*', doinuaren_urla)

    audio_ref_zenbakia = audio_ref_zenbakia.group(0)

    audio_ref_zenbakia = re.sub( pattern = 'mp3a/',string = audio_ref_zenbakia, repl = '')

    return os.path.join(current_dir, audio_ref_zenbakia + '.mp3')




def deskargatu_doinua(audio_file):
    """   """
    doinuaren_urla = audio_file['src']
    urllib.request.urlretrieve( doinuaren_urla, sortu_patha(doinuaren_urla) )
    
    
    
    
def _eskuratu_soinu_urlak(doinu_url_parseatua):
    
    
    try:
        
        
        td_list = doinu_url_parseatua.findAll('td')
                
        doinu_izena = doinu_url_parseatua.findAll('dd')[0].string
        print(doinu_izena)
        dl_horizontal = doinu_url_parseatua.findAll('dl', ["dl-horizontal"])
        
        spans = []
        
        
        for span in dl_horizontal[-1].find_all('span'):
            spans.append(span.string)
            print(spans)
                
        for td_idx in enumerate(td_list):
        
            index = td_idx[0]
            
            title_td = td_idx[1].get('title')
        
        
            if title_td == 'Midia eskuratu':
                
                midi_url = td_idx[1].find('a').get('href')
                mp3_index = index + 2    
                mp3_url = td_list[mp3_index].find('a').get('href')
                
                break 
            
    except:
        
        doinu_izena = ''
        mp3_url = ''
        midi_url = ''
        spans = ['']
            
    return {'title': doinu_izena, 'mp3_url': mp3_url, 'midi_url': midi_url, 'metadata': spans}


def eskuratu_doinu_urlko_soinulinkak(doinu_header):
    
    try:
        doinu_url = doinu_header.find('a').get('href')
        
        doinu_response = requests.get(doinu_url)
    
        doinu_parsed = BeautifulSoup(doinu_response.text, "html.parser")
    
        doinu_hiztegia = _eskuratu_soinu_urlak(doinu_parsed)
     
    except:    
        print('Urla irakurtzen errorea.')
        doinu_hiztegia = {''}
    return doinu_hiztegia

#%%

#eskuratu_doinu_urlko_soinulinkak(h4[1])