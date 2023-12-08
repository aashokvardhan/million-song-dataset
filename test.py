from urllib.request import urlretrieve
from zipfile import ZipFile 
import pandas as pd
import numpy as np
import sqlite3
import pandas as pd 

columns = ['track_id',
 'title',
 'song_id',
 'release',
 'artist_id',
 'artist_mbid',
 'artist_name',
 'duration',
 'artist_familiarity',
 'artist_hotttnesss',
 'year',
 'track_7digitalid',
 'shs_perf',
 'shs_work']

data_url = 'http://millionsongdataset.com/sites/default/files/challenge/train_triplets.txt.zip'
filename = 'train_triplets.txt.zip'
output_folder = "data"

urlretrieve(data_url, filename)

# loading the temp.zip and creating a zip object 
with ZipFile(filename, 'r') as zObject: 
    zObject.extractall(path=output_folder) 

h5_link = 'http://millionsongdataset.com/sites/default/files/AdditionalFiles/track_metadata.db'
filename = 'track_metadata.db'
urlretrieve(h5_link, filename)

conn_tmdb = sqlite3.connect('track_metadata.db')

res = conn_tmdb.execute("SELECT * FROM songs")
data = res.fetchall()

track_metadata = pd.DataFrame(data, columns=columns)
track_metadata.to_csv('track_metadata.csv', index=False)
