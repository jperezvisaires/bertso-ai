#%%

from aux_scraping import eskuratu_doinuen_metadatuak


import os
import pickle

import pandas as pd

#%% Fetching metadata from the web

master_hiztegia = eskuratu_doinuen_metadatuak()  # If left empty reads all


#%% Storing as pandas

doinu_tbl = pd.DataFrame.from_dict(master_hiztegia)

doinu_tbl.to_csv("doinu_meta.csv")

