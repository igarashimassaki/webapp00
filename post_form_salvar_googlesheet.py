# -*- coding: utf-8 -*-
"""POST_Form_Salvar_GoogleSheet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HvcZVodDrPnZ-BvdNxPl1mhzz7F4nDmb
"""

#https://stackoverflow.com/questions/65577892/error-message-http-not-defined-api-import-python
#  data retrieval
import urllib3
from urllib3 import request
# json data
import json
# pandas dataframes
import pandas as pd

# get data from the API
http = urllib3.PoolManager()
link = "https://docs.google.com/forms/d/e/1FAIpQLSeKvAxYtOVVOeMRszKOn7SurA9t6XK5Z7S51fN8N9NXrdRbtA/formResponse?&submit=Submit?usp=pp_url&entry.1517261322=2023-07-23&entry.1359404055=17:35&entry.1740304734=PERIODO&entry.357148735=VALOR&entry.919444125=TX&entry.1139794525=GORJETA"
r = http.request('GET', link)
r.status