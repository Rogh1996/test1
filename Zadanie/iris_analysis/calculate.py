import statistics

def cal_stat(data):
    sl = []
    sw = []
    pl = []
    pw = []
    for i in range(1, len(data)):
        sl.append(float(data[i][0]))
        sw.append(float(data[i][1]))
        pl.append(float(data[i][2]))
        pw.append(float(data[i][3]))
    result = []
    for e in [sl, sw, pl, pw]:
        m = statistics.mean(e)
        me = statistics.median(e)
        sd = statistics.stdev(e)
        result.append([m, me, sd])
    return result