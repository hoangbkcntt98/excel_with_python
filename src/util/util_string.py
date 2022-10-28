import textwrap
import pandas as pd
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