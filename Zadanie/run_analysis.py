import sys
from iris_analysis.io import load
from iris_analysis.io import save
from iris_analysis import calculate

data = load.load_data(sys.argv[1])
result = calculate.cal_stat(data)
save.save_results(result)