import sys
import os
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException

def save_obj(file_path,obj):
    try:
        dir_name=os.path.dirname(file_path)

        os.makedirs(dir_name,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except:
        raise CustomException(e,sys)