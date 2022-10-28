from base64 import encode
from cmath import isnan, nan
from operator import index
import pandas as pd
import numpy as np

def fillTitle(data_xls):
    for i in range(len(data_xls)):
        title_no = data_xls.loc[i, header['title_no']]
        title_name = data_xls.loc[i, header['title_name']]
        if pd.isna(title_no) or pd.isna(title_name):
            title_no = old_title_no
            title_name  = old_title_name
        else:
            old_title_no = title_no
            old_title_name = title_name
        data_xls.loc[i, header['title_no']] = title_no
        data_xls.loc[i, header['title_name']] = title_name
def getLastRow(data_xls, flg_title = 'sentence'):
    for i in range(len(data_xls)):
        flag = data_xls.loc[i, header[flg_title]]
        if pd.isna(flag):
            return i
    return -1
file = 'backend/data/N1_Kanji.xlsx'
kanji_sheet = "K"
reading_range = "B1:K317"
reading_cols = "B:K"
output_dir = "backend/output/"

unnecess_rows = lambda x: x in [1]

header = {
    "no": "順番",
    "title_no": "章番号",
    "title_name": "章名",
    "kanji": "漢字",
    "meaning": "意味",
    "reading": "読み方",
    "remember" :"覚え方",
    "word": "単語",
    "sentence":"例文"
}


data_xls = pd.read_excel(file, kanji_sheet, index_col=None, usecols=reading_cols, skiprows=unnecess_rows)
fillTitle(data_xls)
last_row = getLastRow(data_xls)

data_xls.to_csv(output_dir + "anki_csv.csv", encoding='utf_8', na_rep='NA', index=False, header=False, float_format = "%d")

