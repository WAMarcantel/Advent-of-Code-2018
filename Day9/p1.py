def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list

class Marble:

    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

def insert(nodebefore, nodeafter, val):

    new_node = Marble(val)

    new_node.prev = nodebefore
    nodebefore.next = new_node

    new_node.next = nodeafter
    nodeafter.prev = new_node

    return new_node

def remove(nodebefore, nodeafter):

    nodebefore.next = nodeafter
    nodeafter.prev = nodebefore

def printCircle():

    s = ""

    current_node = zero_marble
    nodeval = -1
    while nodeval != 0:
        s += " " + str(current_node.num)
        current_node = current_node.next
        nodeval = current_node.num

    print(s)


players = int(read_input("input")[0].split()[0])
last_marble_score = int(read_input("input")[0].split()[6])

scores = [0 for i in range(players)]
player = 0
last_score = 0
marble_num = 1

zero_marble = Marble(0)
zero_marble.next = zero_marble
zero_marble.prev = zero_marble

current_marble = zero_marble

for i in range(last_marble_score*100):

    if marble_num % 23 == 0:

        for j in range(6):
            current_marble = current_marble.prev

        last_score = marble_num + current_marble.prev.num
        scores[player] += last_score


        remove(current_marble.prev.prev, current_marble)

    else:
        current_marble = insert(current_marble.next, current_marble.next.next, marble_num)

    print(marble_num)

    player = (player+1) % players
    marble_num += 1


print(max(scores))