#mcandrew

import sys
import numpy as np
import pandas as pd

import requests

if __name__ == "__main__":

    racedata = {"code":[], "race":[]}
    call = requests.get("https://api.census.gov/data/2019/pep/charage/variables/RACE.json")
    if call.ok:
        for code,race in call.json()["values"]["item"].items():
            racedata["race"].append(race)
            racedata["code"].append(code)
    racedata = pd.DataFrame(racedata)
    racedata.to_csv("./pep2019_racedata.csv",index=False)
