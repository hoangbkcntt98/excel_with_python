import textwrap
import pandas as pd
import numpy as np
def wrap(string, lenght=8):
    if type(string) != str:
        return string
    return '\n'.join(textwrap.wrap(string, lenght))

def remove_nan(list):
    newlist = []
    for data in list :
        if pd.isna(data) or data == 'Na':
            newlist.append("")
        else:
            newlist.append(data)
    return newlist
def list_str_to_int(list):
    newList = [int(data) for data in list if data!='']
    if len(newList) ==0:
        return False
    return newList