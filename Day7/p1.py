def read_input(file):
    input_file = open(file)

    list = []
    for line in input_file:

        if line[len(line) - 1] is "\n":
            line = (line[:len(line) - 1])

        list.append(line)
    return list


class Step:
    def __init__(self, name):
        self.predecessors = []
        self.next = []
        self.name = name
        self.done = False


steps = dict()

for item in read_input("input"):
    predecessorname, stepname = item.split()[1], item.split()[7]

    if predecessorname not in steps:
        predStep = Step(predecessorname)
        steps[predecessorname] = predStep

    if stepname not in steps:
        newStep = Step(stepname)
        steps[stepname] = newStep

    steps[predecessorname].next.append(stepname)
    steps[stepname].predecessors.append(predecessorname)

stack = []

for key in steps.keys():
    if not steps[key].predecessors:
        stack.append(key)

doing = []
instructions = ""
time = 0
workercount = 5
wait = False
while stack or doing:

    for working_on in doing:
        if working_on[1] <= time:
            steps[working_on[0]].done = True
            doing.remove(working_on)
            wait = False

    # free worker
    while len(doing) < workercount and not wait and len(stack) > 0:
        stack.sort()
        nextStep = ""
        for i in range(len(stack)):
            isReady = True
            for prev in steps[stack[i]].predecessors:
                isReady = isReady and steps[prev].done

            if isReady and steps[stack[i]] not in [j[0] for j in doing] and not steps[stack[i]].done:
                nextStep = stack.pop(i)
                break

        if nextStep is "":
            wait = True
        else:

            doing.append((nextStep, 60 + time + ord(nextStep) - 64))

            for nextnextStep in steps[nextStep].next:
                if nextnextStep not in stack:
                    stack.append(nextnextStep)

    if not stack and not doing:
        break
    # print(stack)
    # print(doing)
    time += 1

for key in steps.keys():
    if not steps[key].done:
        print(key)

print(time)
