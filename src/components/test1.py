import sys
import os
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score

from sklearn.model_selection import GridSearchCV

def save_obj(file_path,obj):
        dir_name=os.path.dirname(file_path)

        os.makedirs(dir_name,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    