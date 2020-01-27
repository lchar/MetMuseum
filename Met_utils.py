#############################################################
# Testing with a class for Met Museum data                  #
# --------------------------------------------------------- #
# We build here a class in order to modularize the          #
# MetMuseum project files                                   #
#############################################################

import numpy as np
import pandas as pd

class MetData:

    def __init__(self, path):
        self.data = pd.read_csv(path, low_memory=False)
        self.depts = self.data['Department'].unique().tolist()
        
    
    def filter_dep(self, n):
        """
        Function that takes a department index `n` and returns a slice of the data set corresponding to that department.
        """
        return self.data[self.data['Department'] == self.depts[n]]
    
    def gather_text(self, cols):
        text = pd.DataFrame()
        
        text['Object ID'] = self.data['Object ID']
        
        text['text'] = ''
        
        for feat in cols:
            text['text'] = text['text'] + ' ' + self.data[feat].replace(np.nan, '', regex=True)
            
        return text