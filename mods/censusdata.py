#mcandrew

import sys
import numpy as np
import pandas as pd

class pulldatafromCensusServer(object):
    def __init__(self):
        self.callCensus()
    
    def callCensus(self):

        import os
        import requests

        censuskey = os.environ['CENSUSKEY']
        apicall = "https://api.census.gov/data/2019/pep/charage?get=AGE,SEX,POP,RACE&for=us:*&key={:s}".format(censuskey)

        call = requests.get(apicall)
        self.call = call

    def loadData(self):
        import pandas as pd
        i=1
        for line in self.call.json():
            if i:
                order2var = {}
                data = {}
                
                for j,var in enumerate(line):
                    data[var] = []
                    order2var[j] = var
                i=0
            else:
                for j,datum in enumerate(line):
                    data[ order2var[j] ].append(datum)

        self.data = pd.DataFrame(data)

if __name__ == "__main__":
    pass
