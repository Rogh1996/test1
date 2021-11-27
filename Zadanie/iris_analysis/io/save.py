import sys
import csv

def save_results(res):
    with open(sys.argv[2], 'w') as file:
        file = csv.writer(file)
        file.writerow(['name', 'mean', 'median', 'sd'])
        names = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
        for i in range(4):
            file.writerow([names[i]]+res[i])
    return None