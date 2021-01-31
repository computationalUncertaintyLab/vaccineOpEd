#mcandrew

import sys
import numpy as np
import pandas as pd

if __name__ == "__main__":

    pepdata = pd.read_csv("./pepData2019.csv")

    #remove missing age
    pepdata = pepdata.loc[pepdata.AGE<999,:]

    #remove both sexes category
    pepdata = pepdata.loc[pepdata.SEX !=0,:]
    
    #break age into catgeories
    pepdata['agecat'] = pd.cut( pepdata.AGE, [-0.1,18,35,55,65,100]  )
    pepdata['agecat2'] = pd.cut( pepdata.AGE, [-0.1,75,100] )
    pepdata['agecat3'] = pd.cut( pepdata.AGE, [-0.1,65,100] )
    pepdata['agecat4'] = pd.cut( pepdata.AGE, [-0.1,55,100] )
    pepdata['agecat5'] = pd.cut( pepdata.AGE, [-0.1,35,100] )

    pepdata.to_csv("pepData2019_formatted.csv")
