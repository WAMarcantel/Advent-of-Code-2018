def read_input(file):
    input_file = open(file)

    l = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        l.append(line)

    return l


class Cart:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.last_intersection = "right"

    def make_intersection_decision(self):
        if self.last_intersection == "right":
            self.last_intersection = "left"
            self.rotate_counterclockwise()
        elif self.last_intersection == "straight":
            self.last_intersection = "right"
            self.rotate_clockwise()
        else:
            self.last_intersection = "straight"

    def advance_cart(self, tracks):
        self.do_advance()

        if tracks[self.y][self.x] == "+":
            self.make_intersection_decision()
        elif tracks[self.y][self.x] == "\\":
            if self.direction == ">":
                self.direction = "v"
            elif self.direction == "<":
                self.direction = "^"
            elif self.direction == "v":
                self.direction = ">"
            else:
                self.direction = "<"
        elif tracks[self.y][self.x] == "/":
            if self.direction == ">":
                self.direction = "^"
            elif self.direction == "<":
                self.direction = "v"
            elif self.direction == "^":
                self.direction = ">"
            else:
                self.direction = "<"

    def do_advance(self):
        if self.direction == ">":
            self.x += 1
        elif self.direction == "<":
            self.x -= 1
        elif self.direction == "^":
            self.y -= 1
        else:
            self.y += 1

    def rotate_clockwise(self):
        if self.direction == ">":
            self.direction = "v"
        elif self.direction == "v":
            self.direction = "<"
        elif self.direction == "<":
            self.direction = "^"
        else:
            self.direction = ">"

    def rotate_counterclockwise(self):
        if self.direction == ">":
            self.direction = "^"
        elif self.direction == "v":
            self.direction = ">"
        elif self.direction == "<":
            self.direction = "v"
        else:
            self.direction = "<"


def print_tracks(tracks, cart_positions):
    for i in range(len(tracks)):
        s = ""
        for j in range(len(tracks[i])):
            if (j, i) in cart_positions:
                s += 'c'
            else:
                s += tracks[i][j]
        print(s)


tracks = read_input('test')
carts = []

for y in range(len(tracks)):
    for x in range(len(tracks[y])):
        if tracks[y][x] == '>' or tracks[y][x] == '<' or tracks[y][x] == '^' or tracks[y][x] == 'v':
            carts.append(Cart(x, y, tracks[y][x]))

        if tracks[y][x] == '<' or tracks[y][x] == '>':
            tracks[y] = tracks[y][:x] + '-' + tracks[y][x+1:]

        if tracks[y][x] == '^' or tracks[y][x] == 'v':
            tracks[y] = tracks[y][:x] + '|' + tracks[y][x+1:]

cart_positions = set()
old_positions = set((cart.x, cart.y) for cart in carts)
iterations = 0

collisions = []
crash = None
while crash is None:
    old_positions = cart_positions
    cart_positions.clear()
    for cart in carts:
        cart.advance_cart(tracks)
        if (cart.x, cart.y) not in cart_positions and (cart.x, cart.y) not in old_positions:
            cart_positions.add((cart.x, cart.y))

        else:
            crash = (cart.x, cart.y)
            print(crash)
            # collisions.append((cart.x, cart.y))

    # print_tracks(tracks, cart_positions)
    # iterations += 1
    # if iterations == 1000:
    #     crash = (0,0)

# print(collisions)
