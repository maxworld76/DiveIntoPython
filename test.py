
data = [('centos.cpu', 40.0, 1610658809), ('centos.cpu', 41.0, 1610658808), ('centos.cpu', 42.0, 1610658813)]

data_sorted = {}
for metric, value, timestamp in data:
    if metric not in data_sorted:
        data_sorted[metric] = [(value, timestamp)]
    else:
        data_sorted[metric].append((value, timestamp))
    for d in data_sorted.values():
        d.sort(key=lambda tup: tup[1])


print(data_sorted)

