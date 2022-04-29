#%%

import numpy as np
import pandas as pd
import spacy
import time

import requests
from urllib.parse import urlparse
import json
import pickle
#%%
# URL='https://www.youtube.com/watch?v=Yk-unX4KnV4'
# obj=urlparse(URL)
# print(obj.query.replace('v=',''))



def getComments(videoId, maxComments):
        isPageToken=True
        count=0
        PageToken=''
        corpus=[]
        while count<maxComments and isPageToken==True:
                URL="https://www.googleapis.com/youtube/v3/commentThreads"

                parameters={
                        'key': 'AIzaSyCH2b5Euatt-YmsXycpfRBtxtOUammZvL4',
                        'part':'snippet',
                        'videoId':videoId,
                        'textFormat':'plainText',
                        'maxResults':'100'
                        }
                if len(PageToken)>0:
                        parameters['pageToken']=PageToken

                r=requests.get(URL, params=parameters,)

                jsonResponse=r.json()

                corpus.extend([jsonResponse["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for i in range(len(jsonResponse["items"]))])
                
                if 'nextPageToken' in jsonResponse:
                        PageToken=jsonResponse['nextPageToken']
                        isPageToken=True
                else:
                        isPageToken=False
                count+=jsonResponse['pageInfo']['totalResults']
        return corpus

def getVideoCommentSentiments(videoURL): 

        obj=urlparse(videoURL)
        videoId=obj.query.replace('v=','')

        corpus=getComments(videoId, 500)

        nlp=spacy.load(r'C:\Users\dakot\anaconda3\envs\youtube_nlp\Lib\site-packages\en_core_web_lg\en_core_web_lg-3.2.0')

        with nlp.disable_pipes():
                vectors = np.array([nlp(comment).vector for comment in corpus])

        df_vectors=pd.DataFrame(vectors)
        #Test our serialized model before deployment
        modelFile = open('model_svc.p', 'rb')     
        pmodel = pickle.load(modelFile)
        y_predp=pmodel.predict(df_vectors)
        modelFile.close()

        sentimentRatio=list(y_predp).count(1)/(list(y_predp).count(0)+list(y_predp).count(1))

        return [y_predp, sentimentRatio]

#%%
[y_predp_test, ratio]=getVideoCommentSentiments('https://www.youtube.com/watch?v=qfyynHBFOsM')

print(len(y_predp_test))





#%%
URL="https://www.googleapis.com/youtube/v3/commentThreads"
# URL='https://www.googleapis.com/youtube/v3/activities'
parameters={
        'key': 'AIzaSyCH2b5Euatt-YmsXycpfRBtxtOUammZvL4',
        'part':'snippet',
        'videoId':'qfyynHBFOsM',
        'textFormat':'plainText',
        'maxResults':'100'
        }

#parameters['pageToken']=PageToken

r=requests.get(URL, params=parameters,)

jsonResponse=r.json()

print(jsonResponse)

corpus=[jsonResponse["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for i in range(len(jsonResponse["items"]))]

jsonResponse['pageInfo']['totalResults']



#%%


#%%
# URL="https://www.googleapis.com/youtube/v3/commentThreads"
URL='https://www.googleapis.com/youtube/v3/videos'
parameters={
        'key': 'AIzaSyCH2b5Euatt-YmsXycpfRBtxtOUammZvL4',
        'part':'statistics',
        'id': 'xpIFS6jZbe8'
        }

#parameters['pageToken']=PageToken

r=requests.get(URL, params=parameters,)

jsonResponse=r.json()

print(jsonResponse["items"][0]['statistics'])

pd.DataFrame(jsonResponse["items"][0]['statistics'], index=[0])


#%%







