import matplotlib.pyplot as plt

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


points = read_input("input")

seconds = 10325

for j in range(len(points)):
    points[j][0] += points[j][2] * 10325
    points[j][1] += points[j][3] * 10325

for i in range(25):
    seconds += 1
    for j in range(len(points)):
        points[j][0] += points[j][2]
        points[j][1] += points[j][3]

    x = []
    y = []
    for j in range(len(points)):
        x.append(points[j][0])
        y.append(-points[j][1])

    print(seconds)
    plt.scatter(x, y)
    plt.show()

