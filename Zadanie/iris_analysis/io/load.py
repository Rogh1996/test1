import csv

def load_data(file):
    with open(file) as file:
        file = csv.reader(file)
        file = list(file)
    return file