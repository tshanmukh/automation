__author__ = 'Shanmukh'
__status__ = 'Development'

import pandas as pd
from collections import OrderedDict
import json

def getcsv(filename='Endpoints.csv'):
    data = pd.read_csv(filename,usecols=['Source Id', 'Source Type'])
    sourceId=OrderedDict(zip(data['Source Type'],data['Source Id']))
    del sourceId['Node']
    return sourceId


sourceId = getcsv()
print(json.dumps(sourceId))
