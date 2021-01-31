#mcandrew

class grabdata(object):
    def __init__(self,root):
        import os
        self.root = root

    def grabpep(self):
        import os
        import pandas as pd
        
        d = pd.read_csv(os.path.join(self.root,"pepData2019_formatted.csv"))
        print("Importing formatted pepdata 2019")
        return d

if __name__ == "__main__":
    pass
