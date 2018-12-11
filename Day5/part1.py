def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list

def polarity_matches(a, b):
    return ord(a) == ord(b)-32 or ord(a)-32 == ord(b)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def find_polylen(in_str, char):

    in_str = list(filter(lambda x: x!=char and x!=char.upper(), in_str[0]))

    polymer_root = Node(0)
    currentNode = polymer_root

    for char in in_str:
        newNode = Node(char)
        currentNode.next = newNode
        newNode.prev = currentNode
        currentNode = currentNode.next

    currentNode = polymer_root
    while currentNode is not None and currentNode.next is not None and currentNode.next.next is not None:
        if polarity_matches(currentNode.next.val, currentNode.next.next.val):
            if currentNode.next.next.next is not None:
                currentNode.next.next.next.prev = currentNode

            currentNode.next = currentNode.next.next.next
            if currentNode.prev is not None:
                currentNode = currentNode.prev
        else:
            currentNode = currentNode.next

    count = 0
    currentNode = polymer_root.next
    s= ""
    while currentNode is not None:
        count += 1
        s += str(currentNode.val)
        currentNode = currentNode.next

    return count

in_str = read_input("input")

min = float('inf')
for i in range(97, 123):
    p = find_polylen(in_str, chr(i))
    if p < min:
        min = p

print(min)
