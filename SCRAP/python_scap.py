#%% 

from aux_scraping import eskuratu_doinuen_metadatuak


import os
import pickle


#%%

master_hiztegia = eskuratu_doinuen_metadatuak() # If left empty reads all

#%%

#if not os.path.exists('doinu_meta.pkl'):
    
#    master_hiztegia = eskuratu_doinuen_metadatuak()
    
#    with open('doinu_meta.pkl', 'wb') as handle:
#        pickle.dump(master_hiztegia, handle, protocol=pickle.HIGHEST_PROTOCOL)

#%%

