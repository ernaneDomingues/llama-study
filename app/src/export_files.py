import re
import pandas as pd
from io import StringIO
import os

folder_path = 'data'


def tables_tratament(text):
    tables = re.compile(r'((?:\|.+\|(?:\n|\r))+)', re.MULTILINE).findall(text)
    return tables

def transform_md_to_df(text, num_page):
    tables = tables_tratament(text)
    if len(tables) > 0:
        for i, table in enumerate(tables):
            df = pd.read_csv(StringIO(table), sep="|", encoding="utf-8", engine="python").dropna(how="all", axis=1)
            df = df.dropna(how="all", axis=0)
            df.to_csv(fr"{folder_path}\page{num_page}table{i+1}.csv", index=False)

def extract_numbers(text):
    return int(re.search(r'\d+', text).group())


def create_tables():
    files_list = os.listdir(folder_path)
    files_list = [file for file in files_list if file.endswith('.md')]
    files_list = sorted(files_list, key=extract_numbers)

    for i, file in enumerate(files_list):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        transform_md_to_df(text, i+1)