def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list


def parse_claim(claim):
    splitclaim = claim.split()
    id = int(splitclaim[0][1:len(splitclaim[0])])

    coords = splitclaim[2][:len(splitclaim[2]) - 1].split(",")
    x = int(coords[0])
    y = int(coords[1])

    dimensions = splitclaim[3].split("x")
    w = int(dimensions[0])
    l = int(dimensions[1])

    return id, x, y, w, l

def mark_claim(fabric, claim, valid):

    double_marked = 0

    id, x, y, w, l = parse_claim(claim)
    valid[id] = True

    for i in range(x, x+w):
        for j in range(y, y+l):
            if fabric[i][j] != 0:
                valid[fabric[i][j]] = False
                valid[id] = False
                if fabric[i][j] != "#":
                    double_marked += 1
                    fabric[i][j] = "#"
            else:
                fabric[i][j] = id


    return double_marked


valid = dict()

claims = read_input("./Part1Input")

fabric = [[0 for x in range(1000)] for y in range(1000)]

total_double_marked = 0
for claim in claims:
    double_marked = mark_claim(fabric, claim, valid)
    total_double_marked += double_marked

for key in valid:
    if valid[key]:
        print(key)