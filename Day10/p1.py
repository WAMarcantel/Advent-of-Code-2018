import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def read_input(file):
    input_file = open(file)

    l = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        l.append(line)

    processed = []

    for i in range(len(l)):

        x = ""
        y = ""
        vx = ""
        vy = ""
        j = 10
        pos = ""
        vel = ""
        while j != len(l[i]):

            if l[i][j] == ">":

                if x == "":
                    pos.replace(" ", "")
                    x = int(pos.split(",")[0])
                    y = int(pos.split(",")[1])
                    j += 11
                else:
                    vel.replace(" ", "")
                    vx = int(vel.split(",")[0])
                    vy = int(vel.split(",")[1])

            else:
                if x == "":
                    pos += l[i][j]
                else:
                    vel += l[i][j]

            j += 1

        processed.append([x, y, vx, vy])

    return processed

def stddev(l):
    mean = sum(l)/len(l)
    return sum(list(map(lambda x: ((x-mean)/(len(l)-1))**2, l)))

points = read_input("input")

xmax = max(list(map(lambda x: x[0], points)))
xmin = min(list(map(lambda x: x[0], points)))
ymax = max(list(map(lambda x: x[1], points)))
ymin = min(list(map(lambda x: x[1], points)))
print("max: ", xmax, ymax)
print("min: ", xmin, ymin)


stdDev = float("inf")
newstdDev = float(99999999999999)

seconds = 0
print(points[0])

for i in range(len(points)):
    points[i][0] += int(points[i][2]) * 100000
    points[i][1] += int(points[i][3]) * 100000

print(points)

l1 = list(map(lambda x: x[0], points))
l2 = list(map(lambda x: x[1], points))
print(l1)
print(l2)

plt.scatter(l1, l2)
plt.figure().canvas.draw()


while newstdDev < stdDev:
    seconds += 1

    for i in range(len(points)):
        points[i][0] += int(points[i][2])
        points[i][1] += int(points[i][3])

    stdDev = newstdDev

    l = list(map(lambda x: x[0], points))
    xmean = sum(l)/len(l)
    xstddev = sum(list(map(lambda x: ((x-xmean)/(len(l)-1))**2, l)))
    l = list(map(lambda x: x[1], points))
    ymean = sum(l)/len(l)
    ystddev = sum(list(map(lambda x: ((x-xmean)/(len(l)-1))**2, l)))

    # print(xstddev, ystddev)
    newstdDev = xstddev + ystddev
    print(newstdDev, stdDev, seconds)

    # if seconds % 100000 == 0:
    #     print(newstdDev, seconds)
    #     for i


print(newstdDev, seconds)

newList = []

for i in range(len(points)):
    vx = points[i][2]
    vy = points[i][3]

    x = points[i][0] - vx
    y = points[i][1] - vy

    newList.append((x, y, vx, vy))


