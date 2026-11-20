import pandas as pd

def read_file(file_path):
    print("Reading CSV file...")
    df = pd.read_csv(file_path)
    return df


import csv

def read_csv(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data