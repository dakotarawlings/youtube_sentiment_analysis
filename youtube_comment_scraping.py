#%%

import numpy as np
import pandas as pd
import time

import requests
import pandas as pd
import json



#%%

URL="https://www.googleapis.com/youtube/v3/commentThreads"

headers = {
        'Authorization': 'Bearer [YOUR_ACCESS_TOKEN]',
        'Accept': 'application/json'
            }

parameters={
        'part':'snippet',
        'videoId':'Yk-unX4KnV4',
        'textFormat':'plainText'
        }
r=requests.get(URL, params=parameters)

print(r)

jsonResponse=r.json()

print(jsonResponse)