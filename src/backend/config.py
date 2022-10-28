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

import os
full_path = os.path.realpath(__file__)
__src_dir__ = os.path.dirname(full_path)
unnecess_rows = lambda x: x in [1]