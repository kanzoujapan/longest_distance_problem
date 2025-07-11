import sys
from collections import defaultdict






if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())



def element_split(lines):
    station_info = defaultdict(list)
    for line in lines:
        start, end, distance = line[0], line[1], line[2]
        start = int(start)
        end = int(end)
        distance = float(distance)

        station_info[start].append((end, distance))
        station_info[end].append((start, distance))

    return station_info






