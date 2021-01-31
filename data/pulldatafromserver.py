#mcandrew

import sys
sys.path.append("../")

from mods.censusdata import pulldatafromCensusServer

import numpy as np
import pandas as pd

if __name__ == "__main__":

    call = pulldatafromCensusServer()
    call.loadData()

    call.data.to_csv("./pepData2019.csv",index=False)

    
    
