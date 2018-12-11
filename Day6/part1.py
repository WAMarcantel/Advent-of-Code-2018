def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list


in_raw = read_input("input")

anomalies = []
for i in range(len(in_raw)):
    spliti = in_raw[i].split()
    anomalies.append((int(spliti[0][:len(spliti[0]) - 1]), int(spliti[1]), i))

maxx = max(map(lambda x: x[0], anomalies))
maxy = max(map(lambda x: x[1], anomalies))

grid = [[('.') for y in range(maxx + 1)] for x in range(maxy + 1)]

total = dict()

for anomaly in anomalies:
    # print(anomaly[0], anomaly[1])
    grid[anomaly[1]][anomaly[0]] = (anomaly[2])
    total[anomaly[2]] = 0

# for i in range(len(grid)):
#     s = ""
#     for j in range(len(grid[i])):
#         s += str(grid[i][j])
#
#     print(s)

inf = []
region = []

def manhattanDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(len(grid[0])):
    for j in range(len(grid)):

        total = 0

        for anomaly in anomalies:
            total += manhattanDist((anomaly[0], anomaly[1]), (i, j))

        if total < 10000:
            region.append((i, j))

        # if len(closest) > 1:
        #     grid[j][i] = '.'
        # else:
        #     grid[j][i] = closest[0][2]
        #
        #     total[closest[0][2]] += 1
        #
        #     if i == 0 or i == len(grid) -1 or j == 0 or j == len(grid) -1:
        #         if closest[0][2] not in inf:
        #             inf.append(closest[0][2])

# for i in range(len(grid)):
#     s = ""
#     for j in range(len(grid[i])):
#         s += str(grid[i][j])
#
#     print(s)

print(len(region))


# max = 0
# for anomaly in anomalies:
#     if anomaly[2] not in inf:
#        # print(total[anomaly[2]])
#
#        if total[anomaly[2]] > max:
#            max = total[anomaly[2]]
#
#
# print(max)