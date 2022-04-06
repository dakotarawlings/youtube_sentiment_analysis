#%%

import numpy as np
import pandas as pd
import spacy
import time

import requests
import pandas as pd
import json

import pickle


#%%
def getComments(videoId, numComments):
        URL="https://www.googleapis.com/youtube/v3/commentThreads"

        parameters={
                'key': 'AIzaSyCH2b5Euatt-YmsXycpfRBtxtOUammZvL4',
                'part':'snippet',
                'videoId':videoId,
                'textFormat':'plainText',
                'maxResults':'100'
                }
        r=requests.get(URL, params=parameters,)

        jsonResponse=r.json()

        corpus=[jsonResponse["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for i in range(len(jsonResponse["items"]))]

#%%

URL="https://www.googleapis.com/youtube/v3/commentThreads"

parameters={
        'key': 'AIzaSyCH2b5Euatt-YmsXycpfRBtxtOUammZvL4',
        'part':'snippet',
        'videoId':'Yk-unX4KnV4',
        'textFormat':'plainText',
        'maxResults':'10'
        }
r=requests.get(URL, params=parameters,)

jsonResponse=r.json()

corpus=[jsonResponse["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for i in range(len(jsonResponse["items"]))]

#%%
#Pass this into next api call
print(jsonResponse['nextPageToken'])
#print(json.dumps(jsonResponse["items"][19]["snippet"]["topLevelComment"]["snippet"]["textDisplay"], indent=4))

#%%

nlp=spacy.load(r'C:\Users\dakot\anaconda3\envs\youtube_nlp\Lib\site-packages\en_core_web_lg\en_core_web_lg-3.2.0')

with nlp.disable_pipes():
    vectors = np.array([nlp(comment).vector for comment in corpus])

#%%
df_vectors=pd.DataFrame(vectors)
#Test our serialized model before deployment
modelFile = open('model_svc.p', 'rb')     
pmodel = pickle.load(modelFile)
y_predp=pmodel.predict(df_vectors)
modelFile.close()

#%%

print(y_predp)
print(list(y_predp).count(1)/(list(y_predp).count(0)+list(y_predp).count(1)))




